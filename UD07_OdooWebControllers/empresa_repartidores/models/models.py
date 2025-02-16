from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Empleado(models.Model):
    _name = 'empresa_repartidores.empleado'
    _description = 'Empleado de la Empresa'

    name = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)
    dni = fields.Char(string="DNI", required=True)
    telefono = fields.Char(string="Teléfono")
    foto = fields.Binary(string="Foto")
    carnet_ciclomotor = fields.Boolean(string="Carnet de Ciclomotor")
    carnet_furgoneta = fields.Boolean(string="Carnet de Furgoneta")
    
    repartimiento_ids = fields.One2many(
        'empresa_repartidores.repartimiento', 'repartidor_id', string="Repartimientos"
    )

    def get_repartimientos_pendientes(self):
        for rec in self:
            rec.pendientes = rec.repartimiento_ids.filtered(lambda r: r.estado == 'no_eixit')

    pendientes = fields.One2many('empresa_repartidores.repartimiento', compute='get_repartimientos_pendientes', string="Pendientes")


class Vehiculo(models.Model):
    _name = 'empresa_repartidores.vehiculo'
    _description = 'Vehículo de la Empresa'

    name = fields.Char(string="Tipo", required=True)
    matricula = fields.Char(string="Matrícula")
    foto = fields.Binary(string="Foto")
    descripcion = fields.Text(string="Descripción")
    repartimiento_ids = fields.One2many(
        'empresa_repartidores.repartimiento', 'vehiculo_id', string="Repartimientos"
    )

class Cliente(models.Model):
    _name = 'empresa_repartidores.cliente'
    _description = 'Cliente'

    dni = fields.Char(string="DNI", required=True)
    name = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellidos", required=True)
    telefono = fields.Char(string="Teléfono")
    repartimientos_emisor = fields.One2many(
        'empresa_repartidores.repartimiento', 'client_emisor_id', string="Repartimientos Emitidos"
    )
    repartimientos_receptor = fields.One2many(
        'empresa_repartidores.repartimiento', 'client_receptor_id', string="Repartimientos Recibidos"
    )

class Repartimiento(models.Model):
    _name = 'empresa_repartidores.repartimiento'
    _description = 'Repartimiento / Envío'

    code = fields.Integer(
        string="Código", required=True, copy=False, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('empresa_repartidores.repartimiento')
    )
    fecha_inicio = fields.Datetime(string="Fecha y Hora de Inicio", required=True)
    fecha_retorno = fields.Datetime(string="Fecha y Hora de Retorno", required=True)
    fecha_recepcion = fields.Date(string="Fecha de Recepción", required=True)
    repartidor_id = fields.Many2one(
        'empresa_repartidores.empleado', string="Repartidor", required=True
    )
    vehiculo_id = fields.Many2one(
        'empresa_repartidores.vehiculo', string="Vehículo", required=True
    )
    km = fields.Float(string="Kilómetros", required=True)
    peso = fields.Float(string="Peso (kg)", required=True)
    volumen = fields.Float(string="Volumen", required=True)
    observaciones = fields.Text(string="Observaciones")
    estado = fields.Selection([
        ('no_eixit', 'No ha salido'),
        ('de_cami', 'En camino'),
        ('entregada', 'Entregada')
    ], string="Estado", default='no_eixit')
    urgencia = fields.Selection([
        ('organs', 'Órganos humanos'),
        ('aliments_refrigerats', 'Alimentos refrigerados'),
        ('aliments', 'Alimentos'),
        ('alta', 'Alta Prioridad'),
        ('baixa', 'Baja Prioridad')
    ], string="Urgencia", required=True)
    client_emisor_id = fields.Many2one(
        'empresa_repartidores.cliente', string="Cliente Emisor", required=True
    )
    client_receptor_id = fields.Many2one(
        'empresa_repartidores.cliente', string="Cliente Receptor", required=True
    )

    @api.model
    def create(self, vals):
        # Asignación del código mediante secuencia
        if not vals.get('code'):
            seq = self.env['ir.sequence'].next_by_code('empresa_repartidores.repartimiento')
            vals['code'] = seq if seq else 1

        repartidor_id = vals.get('repartidor_id')
        vehiculo_id = vals.get('vehiculo_id')
        km_val = vals.get('km', 0)

        if repartidor_id and vehiculo_id:
            empleado = self.env['empresa_repartidores.empleado'].browse(repartidor_id)
            vehiculo = self.env['empresa_repartidores.vehiculo'].browse(vehiculo_id)
            # Quitamos espacios y forzamos minúsculas para comparar
            tipo_vehiculo = vehiculo.name.lower().strip()

            # Validación de carnets para ciclomotor o furgoneta
            if tipo_vehiculo in ['ciclomotor', 'furgoneta']:
                if tipo_vehiculo == 'ciclomotor' and not empleado.carnet_ciclomotor:
                    raise ValidationError("El empleado no tiene carnet para ciclomotor.")
                if tipo_vehiculo == 'furgoneta' and not empleado.carnet_furgoneta:
                    raise ValidationError("El empleado no tiene carnet para furgoneta.")

            # Repartimientos de más de 10 km no se pueden hacer en bicicleta
            if tipo_vehiculo == 'bicicleta' and km_val > 10:
                raise ValidationError("Los repartimientos de más de 10 km no se pueden realizar en bicicleta.")

            # Repartimientos de menos de 1 km no se pueden hacer en furgoneta
            if tipo_vehiculo == 'furgoneta' and km_val < 1:
                raise ValidationError("Los repartimientos de menos de 1 km no se pueden realizar en furgoneta.")

        # Definimos qué estados consideramos como "activo"
        active_states = ['no_eixit', 'de_cami']

        # Validación: el empleado no debe tener repartimientos activos
        if repartidor_id:
            active_repartimientos = self.search([
                ('repartidor_id', '=', repartidor_id),
                ('estado', 'in', active_states)
            ])
            if active_repartimientos:
                raise ValidationError("El empleado ya está asignado a un viaje activo.")

        # Validación: el vehículo no debe tener repartimientos activos
        if vehiculo_id:
            active_repartimientos = self.search([
                ('vehiculo_id', '=', vehiculo_id),
                ('estado', 'in', active_states)
            ])
            if active_repartimientos:
                raise ValidationError("El vehículo ya está asignado a un viaje activo.")

        return super(Repartimiento, self).create(vals)


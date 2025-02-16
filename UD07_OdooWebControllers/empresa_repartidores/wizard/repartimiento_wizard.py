from odoo import models, fields, api
from odoo.exceptions import ValidationError

class RepartimientoWizard(models.TransientModel):
    _name = 'empresa_repartidores.repartimiento_wizard'
    _description = 'Wizard para la creación de repartimientos'

    repartidor_id = fields.Many2one('empresa_repartidores.empleado', string="Repartidor", required=True)
    vehiculo_id = fields.Many2one('empresa_repartidores.vehiculo', string="Vehículo", required=True)
    fecha_inicio = fields.Datetime(string="Fecha de Inicio", required=True)
    fecha_retorno = fields.Datetime(string="Fecha de Retorno", required=True)
    fecha_recepcion = fields.Date(string="Fecha de Recepción", required=True)
    km = fields.Float(string="Kilómetros", required=True)
    peso = fields.Float(string="Peso (kg)", required=True)
    volumen = fields.Float(string="Volumen", required=True)
    urgencia = fields.Selection([
        ('organs', 'Órganos humanos'),
        ('aliments_refrigerats', 'Alimentos refrigerados'),
        ('aliments', 'Alimentos'),
        ('alta', 'Alta Prioridad'),
        ('baixa', 'Baja Prioridad')
    ], string="Urgencia", required=True)
    client_emisor_id = fields.Many2one('empresa_repartidores.cliente', string="Cliente Emisor", required=True)
    client_receptor_id = fields.Many2one('empresa_repartidores.cliente', string="Cliente Receptor", required=True)
    observaciones = fields.Text(string="Observaciones")

    def action_create_repartimiento(self):
        self.ensure_one()
        # Opcional: aquí se pueden agregar validaciones adicionales antes de crear el repartimiento

        repartiment_vals = {
            'repartidor_id': self.repartidor_id.id,
            'vehiculo_id': self.vehiculo_id.id,
            'fecha_inicio': self.fecha_inicio,
            'fecha_retorno': self.fecha_retorno,
            'fecha_recepcion': self.fecha_recepcion,
            'km': self.km,
            'peso': self.peso,
            'volumen': self.volumen,
            'urgencia': self.urgencia,
            'client_emisor_id': self.client_emisor_id.id,
            'client_receptor_id': self.client_receptor_id.id,
            'observaciones': self.observaciones,
        }
        repartiment = self.env['empresa_repartidores.repartimiento'].create(repartiment_vals)
        # Retornamos una acción para abrir el repartimiento recién creado
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'empresa_repartidores.repartimiento',
            'view_mode': 'form',
            'res_id': repartiment.id,
            'target': 'current',
        }

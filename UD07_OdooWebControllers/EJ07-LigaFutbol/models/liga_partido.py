# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LigaPartido(models.Model):
    # Nombre y descripcion del modelo
    _name = 'liga.partido'
    _description = 'Un partido de la liga'

    # Atributos del modelo

    # Nombre del equipo que juega en casa casa
    equipo_casa = fields.Many2one('liga.equipo',string='Equipo local',)
    # Goles equipo de casa
    goles_casa= fields.Integer()

    # Nombre del equipo que juega fuera
    equipo_fuera = fields.Many2one('liga.equipo',string='Equipo visitante',)
    # Goles equipo de casa
    goles_fuera= fields.Integer()
    
    def action_print_report(self):
        return self.env.ref('liga.report_liga_partido')._get_report_values(self)

    # Constraints de atributos
    @api.constrains('equipo_casa')
    def _check_mismo_equipo_casa(self):
        for record in self:
            if not record.equipo_casa:
                raise models.ValidationError('Debe seleccionarse un equipo local.')
            if record.equipo_casa == record.equipo_fuera:
                raise models.ValidationError('Los equipos del partido deben ser diferentes.')


    # Constraints de atributos
    @api.constrains('equipo_fuera')
    def _check_mismo_equipo_fuera(self):
        for record in self:
            if not record.equipo_fuera:
                raise models.ValidationError('Debe seleccionarse un equipo visitante.')
            if record.equipo_fuera and record.equipo_casa == record.equipo_fuera:
                raise models.ValidationError('Los equipos del partido deben ser diferentes.')

    def actualizoRegistrosEquipo(self):
        """
        Envuelve el método _actualizoRegistrosEquipo usando el contexto para evitar
        recálculos recursivos.
        """
        if self.env.context.get('recalc_in_progress'):
            return
        # Llamamos al método real con el flag en el contexto
        self.with_context(recalc_in_progress=True)._actualizoRegistrosEquipo()

    def _actualizoRegistrosEquipo(self):
        """
        Recalcula la clasificación de los equipos: reinicia los contadores y recorre todos los partidos.
        """
        # 1. Reiniciar las estadísticas de TODOS los equipos
        equipos = self.env['liga.equipo'].search([])
        for equipo in equipos:
            equipo.victorias = 0
            equipo.empates = 0
            equipo.derrotas = 0
            equipo.goles_a_favor = 0
            equipo.goles_en_contra = 0
            equipo.puntos = 0

        # 2. Recorrer cada partido para ajustar la clasificación
        partidos = self.env['liga.partido'].search([])
        for partido in partidos:
            equipo_casa = partido.equipo_casa
            equipo_fuera = partido.equipo_fuera
            goles_casa = partido.goles_casa
            goles_fuera = partido.goles_fuera

            # Si no hay ambos equipos definidos, saltamos este partido
            if not equipo_casa or not equipo_fuera:
                continue

            diferencia_goles = abs(goles_casa - goles_fuera)
            puntos_casa = 0
            puntos_fuera = 0

            if goles_casa > goles_fuera:
                equipo_casa.victorias += 1
                equipo_fuera.derrotas += 1
                if diferencia_goles >= 4:
                    puntos_casa = 4
                    puntos_fuera = -1
                else:
                    puntos_casa = 3
            elif goles_casa < goles_fuera:
                equipo_fuera.victorias += 1
                equipo_casa.derrotas += 1
                if diferencia_goles >= 4:
                    puntos_fuera = 4
                    puntos_casa = -1
                else:
                    puntos_fuera = 3
            else:
                equipo_casa.empates += 1
                equipo_fuera.empates += 1
                puntos_casa = 1
                puntos_fuera = 1

            equipo_casa.goles_a_favor += goles_casa
            equipo_casa.goles_en_contra += goles_fuera
            equipo_fuera.goles_a_favor += goles_fuera
            equipo_fuera.goles_en_contra += goles_casa

            equipo_casa.puntos += puntos_casa
            equipo_fuera.puntos += puntos_fuera

    # Sobrescribo el borrado (unlink)
    def unlink(self):
        # Borro el registro, que es lo que hace el metodo normalmente
        result=super(LigaPartido,self).unlink()
        # Añado que llame a actualizoRegistroEquipo()
        self.actualizoRegistrosEquipo()
        return result

    # Sobreescribo el metodo crear
    @api.model
    def create(self, values):
        # hago lo normal del metodo create
        result = super().create(values)
        # Añado esto: llamo a la funcion que actualiza la clasificacion
        self.actualizoRegistrosEquipo()
        # hago lo normal del metodo create
        return result


    # API onchange para cuando se modifica un partido
    # Aunque onchange envia un registro, hacemos codigo para recalcular
    # http://www.geninit.cn/developer/reference/orm.html
    @api.onchange('equipo_casa', 'goles_casa', 'equipo_fuera', 'goles_fuera')
    def actualizar(self):
        self.actualizoRegistrosEquipo()

    # Método para sumar 2 goles al equipo de casa
    def action_sumar_2_goles_casa(self):
        for record in self:
            record.goles_casa += 2
        self._actualizoRegistrosEquipo()

    def action_sumar_2_goles_fuera(self):
        for record in self:
            record.goles_fuera += 2
        self._actualizoRegistrosEquipo()
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LigaCrearPartidoWizard(models.TransientModel):
    _name = 'liga.crear.partido.wizard'
    _description = 'Wizard para Crear Partido'

    equipo_casa = fields.Many2one('liga.equipo', string="Equipo Local", required=True)
    equipo_fuera = fields.Many2one('liga.equipo', string="Equipo Visitante", required=True)
    goles_casa = fields.Integer(string="Goles Local", default=0)
    goles_fuera = fields.Integer(string="Goles Visitante", default=0)

    def add_crear_partido(self):
        """Crea un nuevo partido con los datos del wizard."""
        self.ensure_one()

        if self.equipo_casa == self.equipo_fuera:
            raise ValidationError("El equipo local y el visitante no pueden ser el mismo.")

        # Crear el partido en el modelo principal
        partido = self.env['liga.partido'].create({
            'equipo_casa': self.equipo_casa.id,
            'goles_casa': self.goles_casa,
            'equipo_fuera': self.equipo_fuera.id,
            'goles_fuera': self.goles_fuera,
        })

        # Actualizar la clasificación de los equipos
        partido.actualizoRegistrosEquipo()

        return {'type': 'ir.actions.act_window_close'}

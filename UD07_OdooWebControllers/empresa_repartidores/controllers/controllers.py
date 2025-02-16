# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class RepartoController(http.Controller):
    @http.route('/reparto/estado/<int:id>', auth='public', type='http')
    def get_estado_reparto(self, id):
        # Buscamos el reparto por el ID
        reparto = request.env['empresa_repartidores.repartimiento'].sudo().search([('id', '=', id)], limit=1)
        
        if reparto:
            # Retornamos solo el estado del reparto en formato JSON
            resultado = reparto.estado
        else:
            resultado = 'Reparto no encontrado'
        
        # Retornamos el resultado como texto, ya que es solo un valor (string)
        return json.dumps(resultado, default=str)

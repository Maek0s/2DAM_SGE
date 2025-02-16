from odoo import http
from odoo.http import request

class LigaPartidoController(http.Controller):

    @http.route('/eliminarempates', type='http', auth='public', methods=['GET'], csrf=False)
    def eliminar_empates(self):
        # Ejecutar consulta SQL para obtener los IDs de los partidos empatados
        request.env.cr.execute("""
            SELECT id FROM liga_partido
            WHERE goles_casa = goles_fuera
        """)
        ids = [row[0] for row in request.env.cr.fetchall()]
        partidos_empatados = request.env['liga.partido'].sudo().browse(ids)
        num_partidos_empatados = len(partidos_empatados)
        partidos_empatados.unlink()
        return "Número de partidos eliminados: {}".format(num_partidos_empatados)
    
    
from odoo import models, api

class ReportLigaPartido(models.AbstractModel):
    _name = 'liga.report_liga_partido'
    _description = 'Informe de Partido de Liga'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['liga.partido'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'liga.partido',
            'docs': docs,
        }
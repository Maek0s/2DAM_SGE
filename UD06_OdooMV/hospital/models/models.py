# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Paciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'Gestión de pacientes'

    name = fields.Char()
    apellidos = fields.Char()
    sintoma = fields.Char()

class Medico(models.Model):
    _name = 'hospital.medico'
    _description = 'Gestión de médicos'

    numIdentificador = fields.Integer()
    name = fields.Char()
    apellidos = fields.Char()

    # Para hacer que el número de identificador sea único
    sql_constraints = [
        ('numIdentificador', 'unique(numIdentificador)',
         'El número de identificador debe ser único')
    ]

class Diagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'Gestión de diagnosticos'

    _rec_name = 'diagnostico'

    idDiagnostico = fields.Integer()
    diagnostico = fields.Char()

    idPaciente = fields.Many2one('hospital.paciente', string="Paciente")
    idMedicos = fields.Many2many('hospital.medico', string="Médicos")
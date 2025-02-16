# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Ciclo(models.Model):
    _name = 'instituto.ciclo'
    _description = 'Gestión de ciclos'

    name = fields.Char()
    
    modulos = fields.Many2many('instituto.modulo', string="Módulos")

class Modulo(models.Model):
    _name = 'instituto.modulo'
    _description = 'Gestión de módulos'

    name = fields.Char()
    
    ciclo = fields.Many2one('instituto.ciclo', string="Ciclo")
    alumnos = fields.Many2many('instituto.alumno', string="Alumnos")
    profesores = fields.Many2many('instituto.profesor', string="Profesor")

class Alumno(models.Model):
    _name = 'instituto.alumno'
    _description = 'Gestión de alumnos'

    name = fields.Char()

    modulos = fields.Many2many('instituto.modulo', string="Modulos inscritos")

class Profesor(models.Model):
    _name = 'instituto.profesor'
    _description = 'Gestión de profesores'

    name = fields.Char()

    modulos = fields.Many2many('instituto.modulo', string="Modulos que imparte")

    
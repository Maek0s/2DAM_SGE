# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date # Incorporamos el date

# Modelo base, creado como modelo abstracto 
# Este modelo lo heredarara el modelo BibliotecaComic
# Y se ha creado puramente con fin didáctico para ver herencia entre modelos
class BaseArchive(models.AbstractModel):
    #Nombre y descripcion del modelo
    _name = 'base.archive'
    _description = 'Fichero abstracto'

    #Introduce el atributo "Activo"
    activo = fields.Boolean(default=True)

    #Introducice metodo "archivar" que invierte el estado de "activo"
    #Recordamos se recive "self" como el modelo entero y no como un registro,
    #por ese motivo debemos iterar
    def archivar(self):
        #Por cada registro del modelo
        for record in self:
            #Cambiamos el valor de activo a su version negada
            record.activo = not record.activo


#Definimos modelo Biblioteca comic
class BibliotecaComic(models.Model):

    #Nombre y descripcion del modelo
    _name = 'biblioteca.comic'
    #Hereda de "base.archive" (el modelo abstracto creado antes)
    _inherit = ['base.archive']

    _description = 'Comic de biblioteca'

    #Parametros de ordenacion por defecto
    _order = 'fecha_publicacion desc, nombre'

    #ATRIBUTOS

    #PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    #Indicamos que atributo sera el que se usara para mostrar nombre.
    #Por defecto es "name", pero si no hay un atributo que se llama name, aqui lo indicamos
    #Aqui indicamos que se use el atributo "nombre"
    _rec_name = 'nombre'
    #Atributo nombre
    nombre = fields.Char('Titulo', required=True, index=True)
    #Atributo para seleccionar entre varios
    estado = fields.Selection(
        [('borrador', 'No disponible'),
         ('disponible', 'Disponible'),
         ('perdido', 'Perdido')],
        'Estado', default="borrador")
    #Campo con HTML (Sanitizado) donde se guarda la descripción del comic
    descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)
    #Dato binario, para guardar un binario (en la vista indicaremos que es una imagen) con la portada del comic
    portada = fields.Binary('Portada Comic')

    #Fecha de publicación
    fecha_publicacion = fields.Date('Fecha publicación')

    #Precio del libro    
    precio = fields.Float('Precio')
    #Numero de paginas. 
    paginas = fields.Integer('Numero de páginas',
        #Hace que este atributo este disponible para este grupo de seguridad 
        #Que en este caso son todos los usuarios
        groups='base.group_user',
        #Establece que si el estado es perdido, el numero de paginas no se puede cambiar
        estados={'perdido': [('readonly', True)]},
        #Texto a mostrar en la ayuda de la interfaza al dejar el ratón encima
        help='Total numero de paginas',
        #Si se pone a true, indica que si este atributo se aplica a distintas empreas en Odoo
        #para cada empresa ponga un valor distintos
        #Esta colocado con fin didactico a false 
        company_dependent=False)
 
    #Valoración lector, indicando como son los datos
    valoracion_lector = fields.Float(
        'Valoración media lectores',
        digits=(14, 4),  # Precision opcional (total, decimales),
    )
    # Relación muchos a muchos de autores utilizando un "partner"
    # de Odoo (Es un elemento que puede ser empresa o individuo)
    # https://stackoverflow.com/questions/22927605/what-is-res-partner
    autor_ids = fields.Many2many('res.partner', string='Autores')

    # Relación con los ejemplares
    ejemplares_ids = fields.One2many('biblioteca.ejemplar', 'comic_id', string="Ejemplares disponibles")

    #Constraints de SQL del modelo
    #Util cuando la constraint se puede definir con sintaxis SQL
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (nombre)', 'El titulo Comic debe ser único.'),
        ('positive_page', 'CHECK(paginas>0)', 'El comic debe tener al menos una página')
    ]

    #Indicamos que esta funcion es una "Constraints" de ese atributos
    #Dicho de otra forma, cada vez que se cambie ese atributo, se lanzara esta funcion
    #Y si la funcion detecta un cambio inadecuado, cambiara una instruccion
    #Util cuando la constraint no se puede definir con sintaxis SQL y debe indicar en una funcion
    @api.constrains('fecha_publicacion')
    def _check_release_date(self):
        # Recorremos el modelo
        for record in self:
            #Comprobamos de cada registro, primero que haya una fecha_publicacion
            #y tras ello, que la fecha no sea posterior a la actual.
            if record.fecha_publicacion and record.fecha_publicacion > fields.Date.today():
                #Si procede, lanzamos una excepcion
                raise models.ValidationError('La fecha de lanzamiento debe ser anterior a la actual')

# Modelo de Ejemplar de Cómic
class BibliotecaEjemplar(models.Model):
    _name = 'biblioteca.ejemplar'
    _description = 'Ejemplar de Cómic'

    comic_id = fields.Many2one('biblioteca.comic', string="Cómic", required=True, ondelete='cascade')
    socio_id = fields.Many2one('biblioteca.socio', string="Prestado a", ondelete='set null')
    fecha_prestamo = fields.Date(string="Fecha de préstamo", default=date.today())
    fecha_devolucion = fields.Date(string="Fecha prevista de devolución")

    @api.constrains('fecha_prestamo', 'fecha_devolucion')
    def _check_fechas(self):
        for record in self:
            if record.fecha_prestamo and record.fecha_prestamo > date.today():
                raise ValidationError("La fecha de préstamo no puede ser posterior al día de hoy.")
            if record.fecha_devolucion and record.fecha_devolucion < date.today():
                raise ValidationError("La fecha prevista de devolución no puede ser anterior al día de hoy.")


#Definimos modelo Liga Equipo, que almacenara información de cada equipo
class BibliotecaSocio(models.Model):

    #Nombre y descripcion del modelo
    _name = 'biblioteca.socio'

    _description = 'Modelo para almacenar socios'

    #Parametros de ordenacion por defecto
    _order = 'nombre'

    #ATRIBUTOS

    #PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    #Indicamos que atributo sera el que se usara para mostrar nombre.
    #Por defecto es "name", pero si no hay un atributo que se llama name, aqui lo indicamos
    #Aqui indicamos que se use el atributo "nombre"
    _rec_name = 'nombre'

    num_socio= fields.Integer("Numero de socio", required=True)
    nombre = fields.Char('Nombre socio', required=True, index=True)
    apellidos = fields.Char('Apellidos socio', required=True, index=True)

    ejemplares_ids = fields.One2many('biblioteca.ejemplar', 'socio_id', string="Ejemplares prestados")

    #Constraints de SQL del modelo
    _sql_constraints = [
        ('socio_uniq', 'UNIQUE (num_socio)', 'El numero de socio debe ser unico.')
    ]

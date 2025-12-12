from odoo import models, fields

class Alumno(models.Model):
    _name = 'instituto.alumno'
    _description = 'Alumno'

    # Estos son los atributos del modulo
    name = fields.Char(string='Nombre y apellidos', required=True)
    dni = fields.Char(string='DNI/NIE')
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')

    # Relacion varios a varios con alumnos-modulos
    modulo_ids = fields.Many2many(
        'instituto.modulo',
        'modulo_alumno_rel', # Nueva tabla generada
        'alumno_id', # Atributo de la nueva tabla
        'modulo_id', # Atributo de la nueva tabla
        string='Módulos matriculados'
    )
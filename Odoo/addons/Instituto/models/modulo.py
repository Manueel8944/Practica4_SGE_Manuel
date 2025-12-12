from odoo import models, fields

class Modulo(models.Model):
    _name = 'instituto.modulo'
    _description = 'Módulo del ciclo formativo'

    # Estos son los atributos del modulo
    name = fields.Char(string='Nombre del módulo', required=True)
    codigo = fields.Char(string='Código')
    
    # Relacion con ciclo, un ciclo puede tener varios modulos y un modulo solo puede estar en un ciclo
    ciclo_id = fields.Many2one('instituto.ciclo', string='Ciclo formativo', ondelete='cascade')
    
    # Relacion con profesor, un profesor puede impartir varios modulos y un modulo solo puede ser impartido por un profesor
    profesor_id = fields.Many2one('instituto.profesor', string='Profesor')

    # Relacion varios a varios con modulos-alumnos
    alumno_ids = fields.Many2many(
        'instituto.alumno',
        'modulo_alumno_rel', # Nueva tabla generada
        'modulo_id', # Atributo de la nueva tabla
        'alumno_id', # Atributo de la nueva tabla
        string='Alumnos matriculados'
    )
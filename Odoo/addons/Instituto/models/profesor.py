from odoo import models, fields

class Profesor(models.Model):
    _name = 'instituto.profesor'
    _description = 'Profesor'

    # Estos son los atributos del modulo
    name = fields.Char(string='Nombre y apellidos', required=True)
    departamento = fields.Char(string='Departamento')
    numero_colegiado = fields.Char(string='Número de identificación laboral')
    
    # Relacion con modulos, un profesor puede impartir varios modulos y un modulo solo puede ser impartido por un profesor
    modulo_ids = fields.One2many('instituto.modulo', 'profesor_id', string='Módulos impartidos')
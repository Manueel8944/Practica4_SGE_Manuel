from odoo import models, fields

class Ciclo(models.Model):
    _name = 'instituto.ciclo'
    _description = 'Ciclo'

    # Estos son los atributos del ciclo
    name = fields.Char(string='Nombre del ciclo', required=True)
    descripcion = fields.Text(string='Descripción')
    
    # Relacion con modulos, un ciclo puede tener varios modulos y un modulo solo puede estar en un ciclo
    modulo_ids = fields.One2many('instituto.modulo', 'ciclo_id', string='Módulos')
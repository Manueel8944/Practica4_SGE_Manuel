from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BibliotecaSocio(models.Model):
    _name = 'biblioteca.socio'
    _description = 'Socio de la biblioteca'

    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    identificador = fields.Char(string='ID Socio', required=True, unique=True)

    prestamo_ids = fields.One2many(
        'biblioteca.ejemplar',  
        'socio_id', 
        string='Ejemplares Prestados'
    )

    def name_get(self):
        result = []
        for record in self:
            nombre_completo = f"{record.nombre} {record.apellido} ({record.identificador})"
            result.append((record.id, nombre_completo))
        return result
from odoo import models, fields

class Paciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'Paciente del hospital'

    name = fields.Char('Nombre y Apellidos', required=True) # El char se diferencia del text de que tiene un limite de caracteres de 255 y text no
    sintomas = fields.Text('Síntomas')
    
    # Es una relacion varios a varios, un paciente puede tener varios medicos y viceversa
    consulta_ids = fields.Many2many('hospital.medico', # Modelo destino (el otro modelo)
                                    'consulta_paciente_medico', # Nombre de la tabla intermedia en la base de datos
                                    'paciente_id', 'medico_id', # Columnas en la tabla intermedia
                                    string='Médicos que lo atendieron')
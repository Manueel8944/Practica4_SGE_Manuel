from odoo import models, fields

class Medico(models.Model):
    _name = 'hospital.medico'
    _description = 'Medico del hospital'

    name = fields.Char('Nombre y Apellidos', required=True)
    
    numero_colegiado = fields.Char('Número de colegiado')
    
    # Es una relacion varios a varios, un paciente puede tener varios medicos y viceversa
    consulta_ids = fields.Many2many('hospital.paciente', # Modelo destino (paciente)
                                    'consulta_paciente_medico', # Nombre de la tabla intermedia en la base de datos
                                    'medico_id', 'paciente_id', # Columnas en la tabla intermedia
                                    string='Pacientes atendidos')
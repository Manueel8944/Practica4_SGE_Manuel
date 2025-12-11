from odoo import models, fields, api

class Consulta(models.Model):
    _name = 'hospital.consulta'
    _description = 'Consulta de un paciente con un médico'

    paciente_id = fields.Many2one('hospital.paciente', string='Paciente', required=True) # Relacion de que un paciente puede tener varias consultas y al reves no
    medico_id = fields.Many2one('hospital.medico', string='Médico', required=True) # Relacion de que un medico puede tener varias consultas y al reves no
    diagnostico = fields.Text('Diagnóstico') # Texto en el que se pone el diagnóstico
    fecha = fields.Datetime('Fecha', default=fields.Datetime.now) # Ponemos la fecha para el momento en el que se crea la consulta
    
    @api.model
    def create(self, vals):
        # Crear la consulta
        record = super().create(vals)
        # Actualizar Many2many del paciente-medico
        if record.paciente_id and record.medico_id: # Verifica si estan los valores llenos
            record.paciente_id.write({'consulta_ids': [(4, record.medico_id.id)]}) # Creamos los registros, el 4 es para añadir sin borrar nada
            record.medico_id.write({'consulta_ids': [(4, record.paciente_id.id)]})
        return record
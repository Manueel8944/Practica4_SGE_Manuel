from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BibliotecaEjemplar(models.Model):
    _name = 'biblioteca.ejemplar'
    _description = 'Ejemplar de cómic prestable'

    comic_id = fields.Many2one(
        'biblioteca.comic',
        string='Cómic',
        required=True,
        ondelete='cascade'
    )

    socio_id = fields.Many2one(
        'biblioteca.socio',
        string='Prestado a'
    )

    fecha_prestamo = fields.Date(string='Fecha de préstamo')
    fecha_devolucion_prevista = fields.Date(string='Fecha prevista de devolución')

    estado = fields.Selection(
        [('disponible', 'Disponible'),
         ('prestado', 'Prestado')],
        string='Estado',
        default='disponible'
    )

    @api.constrains('fecha_prestamo')
    def _check_fecha_prestamo(self):
        """
        La fecha de préstamo no puede ser futura
        """
        hoy = fields.Date.today()
        for record in self:
            if record.fecha_prestamo and record.fecha_prestamo > hoy:
                raise ValidationError('La fecha de préstamo no puede ser posterior al día actual.')

    @api.constrains('fecha_devolucion_prevista')
    def _check_fecha_devolucion(self):
        """
        La fecha prevista de devolución no puede ser anterior al día actual
        """
        hoy = fields.Date.today()
        for record in self:
            if record.fecha_devolucion_prevista and record.fecha_devolucion_prevista < hoy:
                raise ValidationError('La fecha prevista de devolución no puede ser anterior al día actual.')

    @api.onchange('socio_id')
    def _onchange_socio(self):
        """
        Cambia el estado automáticamente según si está prestado o no
        """
        for record in self:
            if record.socio_id:
                record.estado = 'prestado'
            else:
                record.estado = 'disponible'
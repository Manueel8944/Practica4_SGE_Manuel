{
    'name': 'Instituto',
    'version': '1.0',
    'author': 'Manuel',
    'category': 'Tools',
    'summary': 'Gestión de ciclos, módulos, alumnos y profesore',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ciclo_view.xml',
        'views/modulo_view.xml',
        'views/alumno_view.xml',
        'views/profesor_view.xml',
    ],
    'installable': True,
    'application': True,
}
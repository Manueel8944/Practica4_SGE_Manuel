{
    'name': 'Hospital',
    'version': '1.0',
    'author': 'Manuel',
    'category': 'Tools',
    'summary': 'Gestión de Hospital',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/paciente_view.xml',
        'views/medico_view.xml',
        'views/consulta_view.xml',
    ],
    'installable': True,
    'application': True,
}
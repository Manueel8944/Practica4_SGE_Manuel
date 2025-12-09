# -*- coding: utf-8 -*-
{
    # ===============================
    # Información básica del módulo
    # ===============================
    'name': "Biblioteca Comics",  # Título que verá el usuario
    'summary': "Gestión de cómics con categorías y autores",  # Resumen corto

    'description': """
Gestor de Biblioteca de Cómics
-------------------------------------------------
- Crea, clasifica y gestiona cómics.
- Soporte para jerarquías de categorías.
- Relación con autores (partners).
- Sistema de archivado lógico.
- Cómputo de días desde lanzamiento.
    """,

    'author': "Sergi García",
    'website': "http://apuntesfpinformatica.es",
    'category': 'Tools',   # Categoría donde se clasifica en la app store de Odoo
    'version': '0.1',      # Versión de desarrollo inicial

    # ===============================
    # Indicamos que es una aplicación completa
    # ===============================
    'application': True,

    # ===============================
    # Dependencias: otros módulos que deben estar instalados
    # ===============================
    'depends': ['base'],  # Módulo base de Odoo

    # ===============================
    # Archivos cargados con el módulo
    # ===============================
    'data': [
    'security/ir.model.access.csv',
    'views/biblioteca_comic.xml',
    'views/biblioteca_comic_categoria.xml',
    'views/biblioteca_socio.xml',
    'views/biblioteca_ejemplar.xml',
    ],
}

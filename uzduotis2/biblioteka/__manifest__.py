# -*- coding: utf-8 -*-
{
    'name': "Biblioteka",

    'summary': """Bibliotekos valdymas""",

    'summary': """Bibliotekos valdymo programa""",

    'description': """
        Bibliotekos valdymo programa leidžia:
            - Uzregistruoti knyga
            - Knygai priskirti statusa/uzsakyma
            - Atspausdinti PDF ataskaita
            - Issiusti priminima vartotojui apie grazinti veluojama knyga
    """,

    'author': "Marius Kaminskas",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',
    'sequence': -100,
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'board'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/mail_template_data.xml',
        'wizard/report_wizard_view.xml',
        'views/knyga_view.xml',
        'views/uzsakymai_view.xml',
        'views/menu.xml',
        'views/auto_mail.xml',
        'report/ataskaita.xml',
        'report/uzsakymu_details.xml'
        # 'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}
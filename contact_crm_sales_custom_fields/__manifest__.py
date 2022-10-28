# -*- coding: utf-8 -*-
{
    'name': "Contact Crm Sales Custom Fields",

    'summary': """Add Custom Fields To CRM, Sales and Contact""",

    'description': """
        
            In Sale Order Line
            Add Field Named Number of Users 
             
            In Contact
            Add Two Tabs In Contact Company Details And Contact
            Add Smart Button In contact To Get Number of Users In Quotations Related To Contact 
            
            In CRM
            Add fields Amount, payment term and Type
            Add Menu To Configurations Names CRM Type

    """,
    'author': "M.Deeb",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'crm', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/res_partner.xml',
        'views/crm_type.xml',
        'views/crm_lead.xml',
    ],
    'demo': [],
}

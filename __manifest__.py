# -*- coding: utf-8 -*-
{
    'name': "mail_sender",

    'summary': """
        Send mail on behalf of another user """,

    'description': """
        Use SMTP account as the mail from, The real Send as the Sender 
    """,

    'author': "geninit, Jeffery",
    'website': "http://www.geninit.cn",

    'category': 'Utility',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'views/views.xml',
    ],

    'auto_install': True
    
}

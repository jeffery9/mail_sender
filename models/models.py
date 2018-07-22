# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IrMailServer(models.Model):
    _inherit = 'ir.mail_server'

    email = fields.Char(string=u'Email', required=True, help="Email地址, 例如 postmaster@domain.tld")

    @api.model
    def send_email(self, message, mail_server_id=None, smtp_server=None, smtp_port=None, smtp_user=None, smtp_password=None, smtp_encryption=None, smtp_debug=False ):

        origin_mail_form = message['From']
        if mail_server_id:
            message.replace_header('From', self.sudo().browse(mail_server_id).email)
            message['Sender'] = origin_mail_form

        return super(IrMailServer, self).send_email(message, mail_server_id, smtp_server, smtp_port, smtp_user, smtp_password, smtp_encryption, smtp_debug )
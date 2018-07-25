# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IrMailServer(models.Model):
    _inherit = 'ir.mail_server'

    email = fields.Char(string=u'Email', required=True, help="Email地址, 例如 postmaster@domain.tld")
    allow_relay = fields.Boolean(string=u'服务器允许中继', default=False)

    @api.model
    def send_email(self, message, mail_server_id=None, smtp_server=None, smtp_port=None, smtp_user=None, smtp_password=None, smtp_encryption=None, smtp_debug=False, smtp_session=None ):

        origin_mail_form = message['From']
        if mail_server_id:
            mail_server = self.sudo().browse(mail_server_id)
        else:
            mail_server = self.sudo().search([], order='sequence', limit=1)

        message.replace_header('From', mail_server.email)
        if mail_server.allow_relay and origin_mail_form != mail_server.email:
            message['Sender'] = origin_mail_form

        return super(IrMailServer, self).send_email(message, mail_server_id, smtp_server, smtp_port, smtp_user, smtp_password, smtp_encryption, smtp_debug, smtp_session)
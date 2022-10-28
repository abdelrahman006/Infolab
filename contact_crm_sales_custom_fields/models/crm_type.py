# -*- coding: utf-8 -*-

from odoo import models, fields
from random import randint

class CRMType(models.Model):
    _name = "crm.type"
    _description = "CRM Type"

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string="Name", required=True, )
    color = fields.Integer('Color', default=_get_default_color)

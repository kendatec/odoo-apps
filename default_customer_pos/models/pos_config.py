# -*- coding: utf-8 -*-
from odoo import fields, models


class PosConfigInherit(models.Model):
    _inherit = 'pos.config'

    customer_default_id = fields.Many2one('res.partner', string ='Default customer')
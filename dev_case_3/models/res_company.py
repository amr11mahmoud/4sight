# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    retail_price_list = fields.Many2one('product.pricelist', string="Retail Price List", ondelete='set null')

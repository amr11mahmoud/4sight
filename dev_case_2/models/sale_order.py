# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    supplier_id = fields.Many2one(
        'res.partner',
        string="Supplier",
        domain="[('type', '!=', 'private'), ('company_id', 'in', (False, company_id))]")

    supplier_required = fields.Boolean(compute="_compute_is_supplier_required")

    @api.onchange('order_line')
    def onchange_recalc_supplier_required(self):
        self._compute_is_supplier_required()

    def _compute_is_supplier_required(self):
        self.supplier_required = self.is_supplier_required()

    def is_supplier_required(self):
        custom_dropship_enabled = self.env['ir.config_parameter'].sudo().get_param('dev_case_2.custom_dropship')
        supplier_required = False
        have_drop_ship_product = False
        for line in self.order_line:
            have_drop_ship_product = line.is_mto

        if custom_dropship_enabled:
            if self.state not in ("sale", "done") and have_drop_ship_product:
                supplier_required = True

        return supplier_required
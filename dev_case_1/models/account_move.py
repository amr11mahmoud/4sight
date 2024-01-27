from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    prev_invoiced_count = fields.Integer(compute="_compute_prev_invoiced_count")

    def _compute_prev_invoiced_count(self):
        for rec in self:
            moves_ids = self.env['account.move'].search([
                ('date', '<', self.invoice_date),
                ('move_type', '=', "out_invoice"),
                ('state', '=', "posted"),
                '|',
                ('partner_id', '=', self.partner_id.id),
                ('partner_id', '=', self.partner_id.parent_id.id)
            ])
            rec.prev_invoiced_count = self.env['account.move.line'].search_count(
                [('move_id', 'in', moves_ids.ids), ('product_id', '!=', None)])

    def open_prev_invoiced_view(self):
        moves_ids = self.env['account.move'].search([
                ('date', '<', self.invoice_date),
                ('move_type', '=', "out_invoice"),
                '|',
                ('partner_id', '=', self.partner_id.id),
                ('partner_id', '=', self.partner_id.parent_id.id)
            ])

        return {
            'type': 'ir.actions.act_window',
            'name': "Prev Invoices Lines",
            'res_model': 'account.move.line',
            'domain': [('move_id', 'in', moves_ids.ids), ('product_id', '!=', None)],
            'view_mode': 'tree',
            'view_id': self.env.ref('dev_case_1.account_move_line_prev_invoiced_tree_view').id,
            'search_view_id': self.env.ref('dev_case_1.account_move_line_prev_invoiced_search_view').id,
            'target': 'current',
            'context': {'search_default_groupby_product_id': 1}
        }
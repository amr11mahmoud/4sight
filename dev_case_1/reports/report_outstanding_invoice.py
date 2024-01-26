import time
from odoo import api, models


class ReportOutstandingInvoice(models.AbstractModel):
    _name = 'report.dev_case_1.report_outstanding_invoice'
    _description = 'Outstanding Invoice Reports'

    @api.model
    def _get_report_values(self, docids, data=None):
        report = self.env['ir.actions.report']._get_report_from_name('dev_case_1.report_outstanding_invoice')
        current_invoice = self.env[report.model].browse(docids)
        current_invoice.ensure_one()
        docs = []
        outstanding_invoices = self.env['account.move'].search([
            ('state', '=', 'posted'),
            ('move_type', '=', 'out_invoice'),
            ('payment_state', 'in', ('not_paid', 'partial')),
            ('partner_id', '=', current_invoice.partner_id.id)])

        for outstanding_invoice in outstanding_invoices:
            docs.append({
                "reference": outstanding_invoice.name,
                "date": outstanding_invoice.date,
                "invoice_date_due": outstanding_invoice.invoice_date_due,
                "line_ids": outstanding_invoice.invoice_line_ids,
                "residual_amount": outstanding_invoice.amount_residual
            })

        docs_sorted = sorted(docs, key=lambda d: d['invoice_date_due'])

        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': docs_sorted,
            'partner_name': current_invoice.partner_id.display_name,
        }
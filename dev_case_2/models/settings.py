from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    custom_dropship = fields.Boolean(string='Custom Drop-ship',
                                     config_parameter='dev_case_2.custom_dropship',
                                     help='Check this field for enabling custom dropship')
    is_installed_sale = fields.Boolean(string="Is the Sale Module Installed")

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('dev_case_2.custom_dropship', self.custom_dropship)
        return res

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ICP = self.env['ir.config_parameter'].sudo()
        custom_dropship_parameter = ICP.get_param('dev_case_2.custom_dropship')
        res.update(is_installed_sale=self.env['ir.module.module'].search(
            [('name', '=', 'sale'), ('state', '=', 'installed')]).id,
                   custom_dropship=custom_dropship_parameter)
        return res

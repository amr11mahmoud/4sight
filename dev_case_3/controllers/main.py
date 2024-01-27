# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class ProductRetailPriceWebsiteSale(WebsiteSale):
    @http.route(['/shop/<model("product.template"):product>'], type='http', auth="public", website=True, sitemap=True)
    def product(self, product, category='', search='', **kwargs):
        vals = self._prepare_product_values(product, category, search, **kwargs)
        retail_price_list = request.env.company.retail_price_list
        retail_price = product.list_price
        retail_price_currency = request.env.company.currency_id.symbol
        if len(retail_price_list) == 1:
            price_list_item = request.env['product.pricelist.item'].sudo().search([
                ('product_tmpl_id', '=', product.id),
                ('pricelist_id', '=', retail_price_list.id)
            ])
            if len(price_list_item) == 1:
                # TODO Handle other type of pricing strategy
                retail_price = price_list_item.fixed_price
                retail_price_currency = price_list_item.currency_id.symbol

        vals['retail_price'] = retail_price
        vals['retail_price_currency'] = retail_price_currency

        return request.render("website_sale.product", vals)

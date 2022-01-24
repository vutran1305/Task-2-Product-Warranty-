# from addons.account_check_printing.models.res_company import res_company
import json

from odoo import models , fields ,api
class SaleOrderWarranty(models.Model):
    _inherit = 'sale.order.line'
    discount_estimated = fields.Float('Sale order discount estimated"' , default = 0 , related = "product_id.sale_order_discount_estimated")

    @api.onchange("product_uom_qty")
    def _compute_sale_discount_estimated_(self):
        for record in self:
            record.discount_estimated = record.product_id.sale_order_discount_estimated * record.product_uom_qty

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0) - line.discount_estimated/line.product_uom_qty
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty,
                                            product=line.product_id, partner=line.order_id.partner_shipping_id)
            line.update({
                'price_tax': taxes['total_included'] - taxes['total_excluded'],
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })
            if self.env.context.get('import_file', False) and not self.env.user.user_has_groups(
                    'account.group_account_manager'):
                line.tax_id.invalidate_cache(['invoice_repartition_line_ids'], [line.tax_id.id])

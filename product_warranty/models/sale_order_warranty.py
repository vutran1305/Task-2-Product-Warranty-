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
        res = super(SaleOrderWarranty,self)._compute_amount()
        for line in self:
            line.price_subtotal -= line.discount_estimated
        return res




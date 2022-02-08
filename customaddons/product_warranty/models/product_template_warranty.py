from odoo import models , fields ,api
from datetime import datetime
from odoo.exceptions import UserError, ValidationError
class ProducWarranty(models.Model):
    _inherit ='product.template'
    product_warranty = fields.Char("Warranty code" , compute = "_auto_set_warranty_value" )
    date_to = fields.Date("End day" )
    date_from = fields.Date("Start day")
    check_warranty = fields.Boolean("Check Warranty" , default = False)
    sale_order_discount_estimated = fields.Float("Sale order discount estimated" , default = 0 , compute = "_calculated_discount_total")
    time_interval = fields.Char("Time interval" , compute = "_calculate_time_interval")

    @api.onchange('date_to','date_from')
    def _auto_set_warranty_value(self):
        for record in self:
            if not record.date_from or not record.date_to:
                record.product_warranty = ''
                return {}
            else:
                record.product_warranty = 'PWR' + '/' + record.date_from.strftime("%d") + record.date_from.strftime("%m") \
                                        + record.date_from.strftime("%y") + '/' + record.date_to.strftime("%d") + record.date_to.strftime("%m") \
                                        + record.date_to.strftime("%y")



    @api.onchange('date_to', 'date_from')
    def _check_warranty(self):
        for record in self:
            if not record.date_from or not record.date_to:
                record.check_warranty = False
            else:
                date_interval = record.date_to - datetime.now().date()
                count = date_interval.days
                if count < 0:
                    record.check_warranty = False
                else:
                    record.check_warranty = True



    @api.onchange('product_warranty','list_price')
    def _calculated_discount_total(self):
        for record in self:
            if not record.check_warranty:
                record.sale_order_discount_estimated = (record.list_price * 10) / 100
            else:
                record.sale_order_discount_estimated = 0

    @api.onchange('product_warranty')
    def _calculate_time_interval(self):
        for record in self:
            if not record.product_warranty or not record.date_to or not record.date_from:
                record.time_interval = "Không bảo hành"
            else:
                time = (record.date_to - datetime.now().date() ).days
                if time < 0:
                    record.time_interval = "Hết hạn bảo hành"
                elif time ==0 :
                    record.time_interval  = "Trong hôm nay"
                elif time > 366:
                    record.time_interval  = "Còn " + str(time//366) + " năm"
                elif time > 31:
                    record.time_interval = "Còn " + str(time // 30) + " tháng"
                else:
                    record.time_interval = "Còn " + str(time) + " ngày"
























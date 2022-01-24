from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime
import logging

class ProductWarrantyWizard(models.TransientModel):
    _name = 'product.warranty.wizard'
    _description = 'Product warranty wizard'
    date_to = fields.Date("End day")
    date_from = fields.Date("Start day")
    check_warranty = fields.Boolean("Check Warranty", default=False)



    def mass_update_product_warranty(self):
        ids = self.env.context['active_ids']  # selected record ids
        products = self.env["product.template"].browse(ids)

        date_input_valid = self.date_to and self._check_date_input_valid(date_from=self.date_from,date_to=self.date_to)
        if self.date_from and date_input_valid:
            new_data = {"date_to" : self.date_to,
                        "date_from" : self.date_from,
                        "check_warranty" : date_input_valid
                        }
            products.write(new_data)
        else:
            raise ValidationError("Ngày nhập không hợp lệ ")

    @api.model
    def _check_date_input_valid(self,date_from,date_to):
        if (date_to - date_from).days < 0:
            return False
        else:
            return True




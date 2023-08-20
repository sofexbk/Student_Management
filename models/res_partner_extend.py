from odoo import api,fields,models
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta



class SaleOrder(models.Model):
    _inherit='res.partner'
    is_professor=fields.Boolean(string="Is_Prof")



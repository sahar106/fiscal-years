
from odoo import models, fields, api,_

class Settings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    group_fiscal_year = fields.Boolean(implied_group="account.group_account_manager",string="Fiscal Year")
    fiscalyear_last_day = fields.Integer(related='company_id.fiscalyear_last_day',readonly=False)
    fiscalyear_last_month = fields.Selection(related='company_id.fiscalyear_last_month',readonly=False)
    period_lock_date = fields.Date(related='company_id.period_lock_date',readonly = False)
    fiscalyear_lock_date= fields.Date(related='company_id.fiscalyear_lock_date')
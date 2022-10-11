
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ChangeLockDate(models.TransientModel):
    _name = 'change.lock.date'
    _description = 'Change Lock Date'
    
    
    
    @api.model
    def default_get(self, vals):
        res = super(ChangeLockDate, self).default_get(vals)
        print('hi')
        company_rec = self.env.user.company_id
        res.update({
            'company_id': company_rec.id,
            'period_lock_date': company_rec.period_lock_date,
            'fiscalyear_lock_date': company_rec.fiscalyear_lock_date,
            'tax_lock_date': company_rec.tax_lock_date,
        })
        return res
    
    period_lock_date = fields.Date(string='Lock Date for Non-Advisers' ,
                                   default=lambda self: self.env.company.period_lock_date,
                                   help ="Only users with the 'Adviser' role can edit accounts prior to and inclusive of this date. Use it for period locking inside an open fiscal year, for example")
    fiscalyear_lock_date = fields.Date(string ="Lock Date for All Users",
                                       default = lambda self: self.env.company.fiscalyear_lock_date,
                                       help = "No users, including Advisers, can edit accounts prior to and inclusive of this date. Use it for fiscal year locking for example.")
    tax_lock_date = fields.Date(string ="Tax Lock Date",
                                default= lambda self:self.env.company.tax_lock_date,
                                help="No users can edit journal entries related to a tax prior and inclusive of this date.")
    company_id = fields.Many2one('res.company',default= lambda self: self.env.company)
    
    
    def change_lock_date(self):
        if self.env.user.has_group('account.group_account_manager'):
            self.company_id.sudo().write({
                'period_lock_date': self.period_lock_date,
                'fiscalyear_lock_date': self.fiscalyear_lock_date,
                'tax_lock_date':self.tax_lock_date,
            })
        else:
            raise UserError(_('You  are not allowed to change lock date'))
        return {'type':'ir.actions.act_window_close'}
    
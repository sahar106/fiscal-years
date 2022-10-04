# -*- coding: utf-8 -*-
from xml.dom import ValidationErr
from odoo import models, fields, api,_


class fiscal_year(models.Model):
    _name = 'account.fiscal.year'
    _description = 'fiscal year'

    name = fields.Char(required=True)
    date_from = fields.Date(string='Start Date', required=True, help='start date, included in the fiscal year')
    date_to = fields.Date(string='End Date' ,required=True, help='end date, incuded in the fiscal year')
    company_id = fields.Many2one('res.company',required=True, default= lambda self:self.env.company)
    
    @api.constrains('date_from','date_to','company_id')
    def check_date_of_fiscal_year(self):
        for fiscal_y in self:
            date_from = fiscal_y.date_from
            date_to = fiscal_y.date_to
            if date_to < date_from:
                raise ValidationErr(_('the ending date must be after starting date'))
            domain =[
                ('id', '!=',fiscal_y.id),('company_id','=',fiscal_y.company_id),
                '|','|',
                '&',('date_from','<=',fiscal_y.date_from),('date_to','>=',fiscal_y.date_from),
                '&',('date_from','<=',fiscal_y.date_to),('date_to','>=',fiscal_y.date_to),
                '&',('date_from','<=',fiscal_y.date_from),('date_to','>=',fiscal_y.date_to)
            ]
            if self.search_count(domain)>0:
                raise ValidationErr(_('you can not overlap between two years, please correct the start and/or end date'))
            
# -*- coding: utf-8 -*-
# © 2016 ONESTEiN BV (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class HrEmployee(models.Model):

    _inherit = 'hr.employee'

    employee_number = fields.Char('Employee Number', copy=False)

    @api.model
    def create(self, vals):
        number = self.env['ir.sequence'].next_by_code('hr.employee') or '/'
        vals['employee_number'] = number
        return super(HrEmployee, self).create(vals)

    _sql_constraints = [
        ('employee_number',
         'unique (employee_number)',
         'Employee Number must be unique !')
    ]

from email.policy import default

from odoo import fields, models, api, _
from odoo.exceptions import UserError, AccessError, ValidationError
from num2words import num2words


class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('coo', 'COO'),
            ('md', 'MD'),
            ('purchase', 'Purchase'),
            ('rejected', 'Rejected'),
        ], string='State', default='draft', tracking=True
    )

    reject_invisible = fields.Boolean(compute='_compute_check', string='Check Order', default=True)
    amount_text = fields.Char(string='Amount', compute='_compute_amount_text')


    @api.depends('state')
    def _compute_check(self):
        for record in self:
            if record.state == 'coo' and self.env.user.has_group('it_proc_app.group_coo'):
                record.reject_invisible = False

            elif record.state == 'md' and self.env.user.has_group('it_proc_app.group_md'):
                record.reject_invisible = False

            else:
                record.reject_invisible = True

    @api.depends('amount_text')
    def _compute_amount_text(self):
        for record in self:
            if record.amount_total:
                record.amount_text = num2words(record.amount_total, to='currency', lang='en')
            else:
                record.amount_text = 'Zero Taka'

    def action_draft(self):
        self.ensure_one()

        self.write({
            'state': 'coo',
        })

    @api.constrains('order_line')
    def _check_order_lines(self):
        for order in self:
            if not order.order_line:
                raise ValidationError(_('At least one product should be in the order'))

    def action_coo_confirm(self):

        if self.amount_total <= 50000:
            self.write({
                'state': 'purchase'
            })
        else:
            self.write({
                'state': 'md',
            })

    def action_md_approve(self):
        self.write({
            'state': 'purchase',
        })

    def action_rejected(self):
        self.write({
            'state': 'rejected',
        })

    @api.model
    def create(self, vals):

        if not self.env.user.has_group('it_proc_app.group_procurement_team'):
            raise ValidationError("You do not have permission to create Purchase Orders.")

        return super(PurchaseOrderInherit, self).create(vals)

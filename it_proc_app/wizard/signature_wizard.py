# -*- coding: utf-8 -*-

from odoo import api, fields, models

class PurchaseOrderSignatureWizard(models.TransientModel):
    _name = 'purchase.order.signature.wizard'
    _description = 'Purchase Order Signature Wizard'

    purchase_order_id = fields.Many2one('purchase.order', string='Purchase Order', required=True)
    signature_coo = fields.Binary(string='Signature',attachment=True)
    signature_md = fields.Binary(string='Signature', attachment=True)
    coo_invisible = fields.Boolean(string='Invisible', compute='_compute_coo_invisible')
    md_invisible = fields.Boolean(string='Invisible', compute='_compute_md_invisible')


    def _compute_coo_invisible(self):
        for record in self:
            if self.env.user.has_group('it_proc_app.group_coo'):
                record.coo_invisible = False
            else:
                record.coo_invisible = True

    def _compute_md_invisible(self):
        for record in self:
            if self.env.user.has_group('it_proc_app.group_md'):
                record.md_invisible = False
            else:
                record.md_invisible = True


    def action_confirm(self):
        self.ensure_one()
        if self.purchase_order_id and self.signature_coo:
            self.purchase_order_id.write({
                'signature_coo': self.signature_coo,
            })
        elif self.purchase_order_id and self.signature_md:
            self.purchase_order_id.write({
                'signature_md': self.signature_md,
            })
        return {'type': 'ir.actions.act_window_close'} 
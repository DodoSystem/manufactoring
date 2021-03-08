from odoo import api, fields, models

class AccountPayment(models.Model):
    _inherit = 'account.payment'    
                
    dds_partner_dds_company_id = fields.Char(compute='_compute_dds_partner_dds_company_id', store=False, string='Company ID (IČO)')
    dds_partner_dds_tax_id = fields.Char(compute='_compute_dds_partner_dds_tax_id', store=False, string='Tax ID (DIČ)')
    dds_partner_vat = fields.Char(compute='_compute_dds_partner_vat', store=False, string='Tax ID (IČ DPH)')

    @api.depends('partner_id')
    def _compute_dds_partner_dds_company_id(self):
        for payment in self:
            payment.dds_partner_dds_company_id = payment.partner_id.dds_company_id

    @api.depends('partner_id')
    def _compute_dds_partner_dds_tax_id(self):
        for payment in self:
            payment.dds_partner_dds_tax_id = payment.partner_id.dds_tax_id

    @api.depends('partner_id')
    def _compute_dds_partner_vat(self):
        for payment in self:
            payment.dds_partner_vat = payment.partner_id.vat
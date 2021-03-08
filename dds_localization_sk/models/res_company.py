from odoo import api, fields, models

class Company(models.Model):
    _inherit = 'res.company'

    dds_company_id = fields.Char(related='partner_id.dds_company_id', readonly=False)
    dds_tax_id = fields.Char(related='partner_id.dds_tax_id', readonly=False)
    dds_tax_id_hidden = fields.Boolean(string='Hide Tax ID (DIČ)', compute='_compute_dds_tax_id_hidden', readonly=False)
    
    @api.onchange('company_registry')
    def _compute_dds_company_registry(self):
        for rec in self:   
            if rec.partner_id:
                rec.partner_id.dds_company_registry = rec.company_registry
                                
    @api.onchange('country_id')
    def _compute_dds_tax_id_hidden(self):
        for rec in self:              
            if rec.country_id.code == 'CZ':
                rec.dds_tax_id_hidden = True
            else:
                rec.dds_tax_id_hidden = False
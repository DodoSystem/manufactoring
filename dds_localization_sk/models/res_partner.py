from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    dds_tax_id_hidden = fields.Boolean(string='Hide Tax ID (DIČ)', compute='_compute_dds_tax_id_hidden', store=False)

    dds_company_id = fields.Char(string='Company ID (IČO)', help='Company ID (IČO).')
    dds_tax_id = fields.Char(string='Tax ID (DIČ)', help='Tax ID (DIČ).')    
    dds_company_registry = fields.Char(string='Company registry')

    @api.model
    def _commercial_fields(self):
        return super(ResPartner, self)._commercial_fields() + ['dds_company_id', 'dds_tax_id']
       
    @api.depends('company_id')
    def _compute_dds_tax_id_hidden(self):
        for rec in self:   
            rec.dds_tax_id_hidden = self.env.company.dds_tax_id_hidden
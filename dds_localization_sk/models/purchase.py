from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
        
    dds_tax_id_hidden = fields.Boolean(related='company_id.dds_tax_id_hidden')

    dds_partner_name = fields.Char(string='Vendor - Name', compute='_compute_dds_partner_all', store=True)
    dds_partner_dds_company_id = fields.Char(string='Company ID (IČO)', compute='_compute_dds_partner_all', store=True)
    dds_partner_dds_tax_id = fields.Char(string='Tax ID (DIČ)', compute='_compute_dds_partner_all', store=True)
    dds_partner_vat = fields.Char(string='Tax ID (IČ DPH)', compute='_compute_dds_partner_all', store=True)
    dds_partner_street = fields.Char(string='Vendor - Street', compute='_compute_dds_partner_all', store=True)
    dds_partner_street2 = fields.Char(string='Vendor - Street 2', compute='_compute_dds_partner_all', store=True)
    dds_partner_city = fields.Char(string='Vendor - City', compute='_compute_dds_partner_all', store=True)
    dds_partner_zip = fields.Char(string='Vendor - Zip', compute='_compute_dds_partner_all', store=True)
    dds_partner_country = fields.Char(string='Vendor - Country', compute='_compute_dds_partner_all', store=True)
    dds_partner_state = fields.Char(string='Vendor - State', compute='_compute_dds_partner_all', store=True)
        
    @api.depends('partner_id')
    def _compute_dds_partner_all(self):
        for order in self:                
            order.dds_partner_dds_company_id = order.partner_id.dds_company_id
            order.dds_partner_dds_tax_id = order.partner_id.dds_tax_id
            order.dds_partner_vat = order.partner_id.vat
            order.dds_partner_name = order.partner_id.name
            order.dds_partner_street = order.partner_id.street
            order.dds_partner_street2 = order.partner_id.street2
            order.dds_partner_city = order.partner_id.city
            order.dds_partner_zip = order.partner_id.zip
            if order.partner_id.country_id:
                order.dds_partner_country = order.partner_id.country_id.name 
            else:
                order.dds_partner_country = ''
            if order.partner_id.state_id:
                order.dds_partner_state = order.partner_id.state_id.name 
            else:
                order.dds_partner_state = ''
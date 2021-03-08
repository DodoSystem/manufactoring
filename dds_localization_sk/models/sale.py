from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    dds_tax_id_hidden = fields.Boolean(related='company_id.dds_tax_id_hidden')

    dds_partner_name = fields.Char(string='Customer - Name', compute='_compute_dds_partner_all', store=True)
    dds_partner_dds_company_id = fields.Char(string='Company ID (IČO)', compute='_compute_dds_partner_all', store=True)
    dds_partner_dds_tax_id = fields.Char(string='Tax ID (DIČ)', compute='_compute_dds_partner_all', store=True)
    dds_partner_vat = fields.Char(string='Tax ID (IČ DPH)', compute='_compute_dds_partner_all', store=True)
    dds_partner_street = fields.Char(string='Customer - Street', compute='_compute_dds_partner_all', store=True)
    dds_partner_street2 = fields.Char(string='Customer - Street 2', compute='_compute_dds_partner_all', store=True)
    dds_partner_city = fields.Char(string='Customer - City', compute='_compute_dds_partner_all', store=True)
    dds_partner_zip = fields.Char(string='Customer - Zip', compute='_compute_dds_partner_all', store=True)
    dds_partner_country = fields.Char(string='Customer - Country', compute='_compute_dds_partner_all', store=True)
    dds_partner_state = fields.Char(string='Customer - State', compute='_compute_dds_partner_all', store=True)
    
    @api.depends('partner_id')
    def _compute_dds_partner_all(self):
        for sale in self:                
            if sale.partner_id.type == 'invoice':
                sale.dds_partner_dds_company_id = sale.partner_id.parent_id.dds_company_id
                sale.dds_partner_dds_tax_id = sale.partner_id.parent_id.dds_tax_id
                sale.dds_partner_vat = sale.partner_id.parent_id.vat
                sale.dds_partner_name = sale.partner_id.parent_id.name
                sale.dds_partner_street = sale.partner_id.parent_id.street
                sale.dds_partner_street2 = sale.partner_id.parent_id.street2
                sale.dds_partner_city = sale.partner_id.parent_id.city
                sale.dds_partner_zip = sale.partner_id.parent_id.zip
                if sale.partner_id.parent_id.country_id:
                    sale.dds_partner_country = sale.partner_id.parent_id.country_id.name 
                else:
                    sale.dds_partner_country = ''
                if sale.partner_id.parent_id.state_id:
                    sale.dds_partner_state = sale.partner_id.parent_id.state_id.name 
                else:
                    sale.dds_partner_state = ''
            else:
                sale.dds_partner_dds_company_id = sale.partner_id.dds_company_id
                sale.dds_partner_dds_tax_id = sale.partner_id.dds_tax_id
                sale.dds_partner_vat = sale.partner_id.vat
                sale.dds_partner_name = sale.partner_id.name
                sale.dds_partner_street = sale.partner_id.street
                sale.dds_partner_street2 = sale.partner_id.street2
                sale.dds_partner_city = sale.partner_id.city
                sale.dds_partner_zip = sale.partner_id.zip
                if sale.partner_id.country_id:
                    sale.dds_partner_country = sale.partner_id.country_id.name 
                else:
                    sale.dds_partner_country = ''
                if sale.partner_id.state_id:
                    sale.dds_partner_state = sale.partner_id.state_id.name 
                else:
                    sale.dds_partner_state = ''
                
    dds_partner_invoicing_name = fields.Char(string='Invoice address - Name', compute='_compute_dds_partner_invoice_all', store=True)
    dds_partner_invoicing_street = fields.Char(string='Invoice address - Street', compute='_compute_dds_partner_invoice_all', store=True)
    dds_partner_invoicing_street2 = fields.Char(string='Invoice address - Street 2', compute='_compute_dds_partner_invoice_all', store=True)
    dds_partner_invoicing_city = fields.Char(string='Invoice address - City', compute='_compute_dds_partner_invoice_all', store=True)    
    dds_partner_invoicing_zip = fields.Char(string='Invoice address - Zip', compute='_compute_dds_partner_invoice_all', store=True)
    dds_partner_invoicing_country = fields.Char(string='Invoice address - Country', compute='_compute_dds_partner_invoice_all', store=True)
    dds_partner_invoicing_state = fields.Char(string='Invoice address - State', compute='_compute_dds_partner_invoice_all', store=True)
    
    @api.depends('partner_invoice_id')
    def _compute_dds_partner_invoice_all(self):
        for sale in self:
            sale.dds_partner_invoicing_name = sale.partner_invoice_id.name
            sale.dds_partner_invoicing_street = sale.partner_invoice_id.street
            sale.dds_partner_invoicing_street2 = sale.partner_invoice_id.street2
            sale.dds_partner_invoicing_city = sale.partner_invoice_id.city  
            sale.dds_partner_invoicing_zip = sale.partner_invoice_id.zip  
            if sale.partner_invoice_id.country_id:
                sale.dds_partner_invoicing_country = sale.partner_invoice_id.country_id.name 
            else:
                sale.dds_partner_invoicing_country = ''
            if sale.partner_invoice_id.state_id:
                sale.dds_partner_invoicing_state = sale.partner_invoice_id.state_id.name 
            else:
                sale.dds_partner_invoicing_state = ''

    dds_partner_shipping_name = fields.Char(string='Delivery address - Name', compute='_compute_dds_partner_shipping_all', store=True)
    dds_partner_shipping_street = fields.Char(string='Delivery address - Street', compute='_compute_dds_partner_shipping_all', store=True)
    dds_partner_shipping_street2 = fields.Char(string='Delivery address - Street 2', compute='_compute_dds_partner_shipping_all', store=True)
    dds_partner_shipping_city = fields.Char(string='Delivery address - City', compute='_compute_dds_partner_shipping_all', store=True)
    dds_partner_shipping_zip = fields.Char(string='Delivery address - Zip', compute='_compute_dds_partner_shipping_all', store=True)
    dds_partner_shipping_country = fields.Char(string='Delivery address - Country', compute='_compute_dds_partner_all', store=True)
    dds_partner_shipping_state = fields.Char(string='Delivery address - State', compute='_compute_dds_partner_all', store=True)
    
    @api.depends('partner_shipping_id')
    def _compute_dds_partner_shipping_all(self):
        for sale in self:
            sale.dds_partner_shipping_name = sale.partner_shipping_id.name
            sale.dds_partner_shipping_street = sale.partner_shipping_id.street
            sale.dds_partner_shipping_street2 = sale.partner_shipping_id.street2
            sale.dds_partner_shipping_city = sale.partner_shipping_id.city  
            sale.dds_partner_shipping_zip = sale.partner_shipping_id.zip  
            if sale.partner_shipping_id.country_id:
                sale.dds_partner_shipping_country = sale.partner_shipping_id.country_id.name 
            else:
                sale.dds_partner_shipping_country = ''
            if sale.partner_shipping_id.state_id:
                sale.dds_partner_shipping_state = sale.partner_shipping_id.state_id.name 
            else:
                sale.dds_partner_shipping_state = ''
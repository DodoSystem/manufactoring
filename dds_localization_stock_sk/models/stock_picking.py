from odoo import api, fields, models

class Picking(models.Model):
    _inherit = 'stock.picking'
    
    dds_partner_name = fields.Char(string='Partner - Name', compute='_compute_dds_partner_all', store=True)
    dds_partner_dds_company_id = fields.Char(string='Company ID (IČO)', compute='_compute_dds_partner_all', store=True)
    dds_partner_dds_tax_id = fields.Char(string='Tax ID (DIČ)', compute='_compute_dds_partner_all', store=True)
    dds_partner_vat = fields.Char(string='Tax ID (IČ DPH)', compute='_compute_dds_partner_all', store=True)
    dds_partner_street = fields.Char(string='Partner - Street', compute='_compute_dds_partner_all', store=True)
    dds_partner_street2 = fields.Char(string='Partner - Street 2', compute='_compute_dds_partner_all', store=True)
    dds_partner_city = fields.Char(string='Partner - City', compute='_compute_dds_partner_all', store=True)
    dds_partner_zip = fields.Char(string='Partner - Zip', compute='_compute_dds_partner_all', store=True)
    dds_partner_country = fields.Char(string='Partner - Country', compute='_compute_dds_partner_all', store=True)
    dds_partner_state = fields.Char(string='Partner - State', compute='_compute_dds_partner_all', store=True)
    
    dds_partner_shipping_name = fields.Char(string='Delivery address - Name', compute='_compute_dds_partner_all', store=True)
    dds_partner_shipping_street = fields.Char(string='Delivery address - Street', compute='_compute_dds_partner_all', store=True)
    dds_partner_shipping_street2 = fields.Char(string='Delivery address - Street 2', compute='_compute_dds_partner_all', store=True)
    dds_partner_shipping_city = fields.Char(string='Delivery address - City', compute='_compute_dds_partner_all', store=True)    
    dds_partner_shipping_zip = fields.Char(string='Delivery address - Zip', compute='_compute_dds_partner_all', store=True)
    dds_partner_shipping_country = fields.Char(string='Delivery address - Country', compute='_compute_dds_partner_all', store=True)
    dds_partner_shipping_state = fields.Char(string='Delivery address - State', compute='_compute_dds_partner_all', store=True)
    
    @api.depends('partner_id')
    def _compute_dds_partner_all(self):
        for move in self:    
            move.dds_partner_shipping_name = move.partner_id.name 
            move.dds_partner_shipping_street = move.partner_id.street
            move.dds_partner_shipping_street2 = move.partner_id.street2
            move.dds_partner_shipping_city = move.partner_id.city    
            move.dds_partner_shipping_zip = move.partner_id.zip            
            if move.partner_id.country_id:
                move.dds_partner_shipping_country = move.partner_id.country_id.name 
            else:
                move.dds_partner_shipping_country = ''  
            if move.partner_id.state_id:
                move.dds_partner_shipping_state = move.partner_id.state_id.name 
            else:
                move.dds_partner_shipping_state = ''

            if move.partner_id.type == 'delivery':
                move.dds_partner_dds_company_id = move.partner_id.parent_id.dds_company_id
                move.dds_partner_dds_tax_id = move.partner_id.parent_id.dds_tax_id
                move.dds_partner_vat = move.partner_id.parent_id.vat
                move.dds_partner_name = move.partner_id.parent_id.name
                move.dds_partner_street = move.partner_id.parent_id.street
                move.dds_partner_street2 = move.partner_id.parent_id.street2
                move.dds_partner_city = move.partner_id.parent_id.city
                move.dds_partner_zip = move.partner_id.parent_id.zip
                if move.partner_id.parent_id.country_id:
                    move.dds_partner_country = move.partner_id.parent_id.country_id.name 
                else:
                    move.dds_partner_country = ''
                if move.partner_id.parent_id.state_id:
                    move.dds_partner_state = move.partner_id.parent_id.state_id.name 
                else:
                    move.dds_partner_state = ''
            else:
                move.dds_partner_dds_company_id = move.partner_id.dds_company_id
                move.dds_partner_dds_tax_id = move.partner_id.dds_tax_id
                move.dds_partner_vat = move.partner_id.vat
                move.dds_partner_name = move.partner_id.name
                move.dds_partner_street = move.partner_id.street
                move.dds_partner_street2 = move.partner_id.street2
                move.dds_partner_city = move.partner_id.city
                move.dds_partner_zip = move.partner_id.zip
                if move.partner_id.country_id:
                    move.dds_partner_country = move.partner_id.country_id.name 
                else:
                    move.dds_partner_country = ''
                if move.partner_id.state_id:
                    move.dds_partner_state = move.partner_id.state_id.name 
                else:
                    move.dds_partner_state = ''
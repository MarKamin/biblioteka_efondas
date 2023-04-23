from odoo import fields, models

class UzsakymasReportWizard(models.TransientModel):
    _name = "uzsakymas.report.wizard"
    _description = "Sukurti uzsakymu ataskaita"

    partner = fields.Many2one('res.partner', string='Vartotojas:')
    date_from = fields.Date(string='Nuo:')
    date_to = fields.Date(string='Iki:')

    def action_create_ataskaita(self):
        domain = []
        partner = self.partner
        if partner:
            domain = domain + [('partner', '=', partner.id)]
        uzsakymai = self.env['uzsakymas.model'].search_read(domain)
        data = {
            'form_data': self.read()[0],
            'uzsakymai': uzsakymai
        }
        return self.env.ref('biblioteka.ataskaita_uzsakymu_details').report_action(self, data=data)
        

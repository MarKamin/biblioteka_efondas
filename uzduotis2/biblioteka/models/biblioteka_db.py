from odoo import fields, models, api
from datetime import datetime, timedelta

class Knyga(models.Model):
    _name = "knyga.model"
    _description = "Knygos modelis"

    name = fields.Char('Knygos pavadinimas', required=True, size=100)
    description = fields.Text('Aprasymas', required=True) 
    pages = fields.Integer('Psl kiekis', required=True)
    genre = fields.Many2many('zanras.model', 'genre_id', string='Knygos zanras')
    knyga = fields.Many2many('uzsakymas.model', 'knyga', string='Knygos uzsakymas')
    
class Zanras(models.Model):
    _name = "zanras.model"
    _description = "Zanro modelis"
    _rec_name = 'genre'

    genre = fields.Char('Knygos zanras', required=True, size=100)
    genre_id = fields.Many2many('knyga.model', string='Knyga')

class Uzsakymas(models.Model):
    _name = "uzsakymas.model"
    _description = "Uzsakymo modelis"
    partner = fields.Many2one('res.partner', string='Klientas')
    _rec_name = 'partner'

    knyga = fields.Many2many('knyga.model', string='Knyga')
    visu_knygu_pav = fields.Char(compute='_compute_visu_knygu_pav', store=True, default='')

    isdavimo_data = fields.Datetime(string='Isdavimo data')
    grazinimo_data = fields.Datetime(string='Grazinimo data')
    busena = fields.Selection([('rezervuota', 'Rezervuota'), ('isduota', 'Isduota'),
                                ('grazinta', 'Grazinta'), ('atsaukta', 'Atsaukta'),], string='Busena')
    
    @api.depends('knyga')
    def _compute_visu_knygu_pav(self):
        for rec in self:
            names = rec.knyga.mapped('name')
            rec.visu_knygu_pav = ', '.join(names)

    @api.onchange('knyga')
    def _onchange_visu_knygu_pav(self):
        self.visu_knygu_pav = ', '.join(self.knyga.mapped('name'))

    @api.model
    def zinute_uz_velavima(self):
        template = self.env.ref("biblioteka.reminder_mail_email")
        irasai = self.search([])
        for rec in irasai:
            if rec.partner.email:
                if rec.busena == 'isduota' and (rec.grazinimo_data <= (datetime.now() + timedelta(hours=3)) ):
                    template.send_mail(rec.id, force_send=True)
                else:
                    pass
        



        
        
                
    

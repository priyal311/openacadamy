from odoo import models, fields, api

class SessionModel(models.Model):
    _name = 'session.model'
    _description = 'session details'

    name = fields.Text(string='session Name')
    start_date = fields.Date(string='session date')
    duration = fields.Integer(string='session duration')
    seats = fields.Integer(string='number of seats')
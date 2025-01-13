from odoo import models, fields, api

class CourseModel(models.Model):
    _name = 'course.model'
    _description = 'course details'


    title = fields.Text(string='course Name')
    description = fields.Text(string='course details')


from odoo import models, fields, api


class Session(models.Model):

    _name = 'academy.session'
    _description = "Session Info"

    course_id = fields.Many2one(
        comodel_name="academy.course",
        string="Course",
        on_delete="cascade",
        required=True
    )

    name = fields.Char(
        string="Title",
        related="course_id.name"
    )

    instructor = fields.Many2one(
        comodel_name="res.partner",
        string="Instructor"
    )

    student_ids = fields.Many2many(
        comodel_name="res.partner",
        string="Students"
    )

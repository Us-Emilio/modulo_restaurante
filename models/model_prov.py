# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Prov(models.Model): 
    _name = "rest.prov"

    name = fields.Char(
        string="Nombre",
        required=True
        )
    starus = fields.Selection(selection=[("preferente", "Preferente"), ("secundario", "Secundario")])
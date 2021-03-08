# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Prov(models.Model): 
    _name = "rest.prov"

    name = fields.Char(
        string="Nombre",
        required=True
        )
    
    emal = fields.Char(
        string="Correo electronico",
        required=True
        )

    num_prov = fields.Integer(
        string="Numero de telefono"
        )
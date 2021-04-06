# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ingrediente(models.Model): 
    _name = "rest.ingrediente"

    name = fields.Char(
        string="Nombre",
        required=True
        )
    
    prov = fields.Many2one("rest.prov", string="Proveedor")

    unidades = fields.Integer(
        string="Unidades",
        required=True
        )
    
    categoria = fields.Selection(
        string="Categoria",
        selection=[("pescado", "Pescado"), ("carne", "Carne"), ("fruta", "Fruta"), ("otros", "Otros")]
        )
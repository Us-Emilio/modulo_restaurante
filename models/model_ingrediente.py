# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ingrediente(models.Model): 
    _name = "rest.ingrediente"

    name = fields.Char(
        string="Nombre",
        required=True
        )
    
    prov = fields.Char(
        string="Proveedor",
        required=True
        )

    unidades = fields.Integer(
        string="Unidades"
        )
    
    cateforia = fields.Selection(
        string="Categoria",
        selection=[("pescado", "Pescado"), ("carne", "Carne"), ("fruta", "Fruta"), ("otros", "Otros")]
        )
    
    cateforia = fields.Selection(
        string="Categoria",
        selection=[("pescado", "Pescado"), ("carne", "Carne"), ("fruta", "Fruta"), ("otros", "Otros")]
        )
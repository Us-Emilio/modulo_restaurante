# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pedidp(models.Model): 
    _name = "rest.pedido"

    remitente = fields.Char(
        string="Remitente",
        required=True
        )
    
    ingrediente = fields.Many2many("rest.ingrediente", string="Ingrediente")

    cantidad = fields.Integer(
        string="Cantidad"
        )
    
    tipo = fields.Selection(
        string="Unidad",
        selection=[("g", "g"),("kg", "Kg"),("unidades", "Unidades")]
        )

    estado = fields.Selection(
        string="Estado",
        selection=[("enviado", "Enviado"),("tramitado", "Tramitado"), ("recivido", "Recivido")]
        )
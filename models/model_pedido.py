# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pedidp(models.Model): 
    _name = "rest.pedido"

    remitente = fields.Char(
        string="Remitente",
        required=True
        )
    
    ingrediente = fields.Char(
        string="Ingrediente",
        required=True
        )

    cantidad = fields.Integer(
        string="Cantidad"
        )
    
    tipo = fields.Selection(
        string="Unidad",
        selection=[("kg", "Kg"),("unidades", "Unidades")]
        )

    estado = fields.Selection(
        string="Estado",
        selection=[("enviado", "Enviado"),("tramitado", "Tramitado"), ("recivido", "Recivido")]
        )
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pedidp(models.Model): 
    _name = "rest.pedido"

    remitente = fields.Char(
        string="Remitente",
        required=True
        )
    
    ingrediente = fields.Many2one("rest.ingrediente", 
        string="Ingrediente",
        required=True)

    cantidad = fields.Float(
        string="Cantidad",
        required=True
        )
    
    tipo = fields.Selection(
        string="Unidad",
        selection=[("g", "g"),("kg", "Kg"),("unidades", "Unidades")],
        required=True
        )
    
    fecha = fields.Date(
        string="Fecha prevista",
        required=True
        )

    estado = fields.Selection(
        string="Estado",
        selection=[("enviado", "Enviado"),("tramitado", "Tramitado"), ("recivido", "Recivido")]
        )

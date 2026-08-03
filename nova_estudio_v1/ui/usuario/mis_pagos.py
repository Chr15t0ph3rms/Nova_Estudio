import flet as ft


def mis_pagos(page: ft.Page, usuario=None):

    # BLOQUEADO: igual que mis_eventos.py, la tabla "pago" (vía "contrato")
    # no tiene relación con un cliente específico todavía.
    # Falta agregar id_cliente en contrato (o en pago) para poder filtrar.

    return ft.Container(
        expand=True,
        padding=20,

        content=ft.Column(
            [
                ft.Text("Mis Pagos", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Divider(),
                ft.Text(
                    "Esta sección estará disponible próximamente.",
                    color=ft.Colors.WHITE70,
                ),
            ],
            expand=True,
        ),
    )

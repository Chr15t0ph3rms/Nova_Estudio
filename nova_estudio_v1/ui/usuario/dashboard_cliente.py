import flet as ft

from ui.components.sidebar import sidebar
from ui.components.navbar import navbar
from ui.components.cards import card

from dao.paquetes_dao import PaquetesDAO
from dao.dj_dao import DjDAO

from ui.usuario.paquetes import paquetes as vista_paquetes
from ui.usuario.djs import djs as vista_djs
from ui.usuario.mis_eventos import mis_eventos
from ui.usuario.mis_pagos import mis_pagos

def dashboard_cliente(page: ft.Page, cerrar_sesion, usuario):

    contenido = ft.Container(expand=True)

    MENU_CLIENTE = [
        (ft.Icons.DASHBOARD, "Dashboard"),
        (ft.Icons.CELEBRATION, "Paquetes"),
        (ft.Icons.MUSIC_NOTE, "DJs"),
        (ft.Icons.EVENT, "Mis Eventos"),
        (ft.Icons.PAYMENTS, "Mis Pagos"),
    ]

    # Dashboard

    def mostrar_dashboard():

        total_paquetes = len(PaquetesDAO().obtener_todo())
        total_djs = len(DjDAO().obtener_todo())

        contenido.content = ft.Column(
            [
                navbar(page, usuario),

                ft.Container(height=20),

                ft.Row(
                    [
                        card("Paquetes disponibles", total_paquetes, ft.Icons.CELEBRATION),
                        card("DJs disponibles", total_djs, ft.Icons.MUSIC_NOTE),
                    ],
                    spacing=20,
                ),

                ft.Container(height=25),

                ft.Container(
                    expand=True,
                    bgcolor=ft.Colors.GREY_900,
                    border_radius=15,
                    padding=25,
                    content=ft.Column(
                        [
                            ft.Text(
                                f"Bienvenido, {usuario.get('nombre', '')}",
                                size=26,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),

                            ft.Divider(),

                            ft.Text("Desde aquí puedes revisar:", size=17, color=ft.Colors.WHITE),

                            ft.Text("• Paquetes disponibles", color=ft.Colors.WHITE),
                            ft.Text("• DJs disponibles", color=ft.Colors.WHITE),
                            ft.Text("• Tus eventos y pagos", color=ft.Colors.WHITE),
                        ]
                    ),
                ),
            ],
            expand=True,
        )

        page.update()

    # Confirmar cierre (igual que en dashboard_admin)

    def confirmar_cierre():

        def aceptar(e):
            cerrar_sesion()

        def cancelar(e):
            mostrar_dashboard()

        contenido.content = ft.Container(
            expand=True,
            bgcolor=ft.Colors.GREY_900,
            border_radius=15,
            padding=30,

            content=ft.Column(
                [
                    ft.Text("Cerrar sesión", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text("¿Seguro que deseas salir?", size=18, color=ft.Colors.WHITE),

                    ft.Row(
                        [
                            ft.ElevatedButton("Cancelar", on_click=cancelar),
                            ft.ElevatedButton("Aceptar", on_click=aceptar),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

        page.update()

    # Cambio de pantallas

    def cambiar_pantalla(opcion):

        pantallas = {
            "Paquetes": vista_paquetes,
            "DJs": vista_djs,
            "Mis Eventos": mis_eventos,
            "Mis Pagos": mis_pagos,
        }

        if opcion == "Dashboard":
            mostrar_dashboard()
            return

        if opcion == "Cerrar sesión":
            confirmar_cierre()
            return

        if opcion in pantallas:
            contenido.content = pantallas[opcion](page, usuario)
            page.update()

    mostrar_dashboard()

    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.BLACK,
        padding=15,

        content=ft.Row(
            [
                sidebar(cambiar_pantalla, opciones=MENU_CLIENTE),

                ft.VerticalDivider(width=1),

                ft.Container(expand=True, content=contenido),
            ],
            expand=True,
        ),
    )

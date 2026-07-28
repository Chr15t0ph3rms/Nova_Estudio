import flet as ft


def sidebar(on_change=None):

    def item(icono, texto):
        return ft.Container(
            border_radius=10,
            padding=10,
            ink=True,
            content=ft.Row(
                [
                    ft.Icon(icono, color=ft.Colors.WHITE),
                    ft.Text(
                        texto,
                        color=ft.Colors.WHITE,
                        size=15,
                    ),
                ],
                spacing=15,
            ),
            on_click=lambda e: on_change(texto) if on_change else None,
        )

    return ft.Container(
        width=250,
        bgcolor=ft.Colors.GREY_900,
        padding=20,
        content=ft.Column(
            [
                ft.Image(
                    src="assets/logo.png",
                    width=120,
                    height=120,
                ),

                ft.Text(
                    "DJ STAFF NOVA",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),

                ft.Divider(),

                item(ft.Icons.DASHBOARD, "Dashboard"),
                item(ft.Icons.PEOPLE, "Clientes"),
                item(ft.Icons.BADGE, "Empleados"),
                item(ft.Icons.LIBRARY_MUSIC, "DJs"),
                item(ft.Icons.EVENT, "Eventos"),
                item(ft.Icons.CELEBRATION, "Paquetes"),
                item(ft.Icons.INVENTORY, "Inventario"),
                item(ft.Icons.PAYMENTS, "Pagos"),
                item(ft.Icons.DESCRIPTION, "Contratos"),
                item(ft.Icons.INSERT_CHART, "Reportes"),
                item(ft.Icons.SETTINGS, "Configuración"),

                ft.Container(expand=True),

                ft.Divider(),

                item(ft.Icons.LOGOUT, "Cerrar sesión"),
            ],
            expand=True,
        ),
    )
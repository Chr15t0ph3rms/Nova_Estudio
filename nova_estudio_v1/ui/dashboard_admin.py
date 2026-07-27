import flet as ft

def dashboard_view(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.add(
        ft.Column(
            [
                ft.Text("Panel de administración", size=22, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                ft.Row(
                    [
                        ft.Container(ft.Text("Servicios: 12", color=ft.colors.WHITE), bgcolor=ft.colors.GREY_900, padding=20, border_radius=8),
                        ft.Container(ft.Text("Eventos: 8", color=ft.colors.WHITE), bgcolor=ft.colors.GREY_900, padding=20, border_radius=8),
                        ft.Container(ft.Text("Usuarios: 25", color=ft.colors.WHITE), bgcolor=ft.colors.GREY_900, padding=20, border_radius=8),
                        ft.Container(ft.Text("Mensajes: 5", color=ft.colors.WHITE), bgcolor=ft.colors.GREY_900, padding=20, border_radius=8),
                    ],
                    spacing=10,
                ),
                ft.Text("Calendario - Mayo 2025", color=ft.colors.GREY_300),
                ft.Text("Actividad reciente", color=ft.colors.GREY_300),
            ],
            spacing=20,
        )
    )

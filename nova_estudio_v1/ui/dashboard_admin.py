import flet as ft

def dashboard_admin_view(page: ft.Page):
    return ft.Container(
        expand=True,
        bgcolor="#1e1e2f",
        content=ft.Column(
            controls=[
                ft.Text("Panel de Administrador", size=30, weight=ft.FontWeight.BOLD, color="white"),
                ft.Row([
                    ft.Card(content=ft.Container(ft.Text("Usuarios: 1,250", color="white"), padding=20, bgcolor="#2a2a3d")),
                    ft.Card(content=ft.Container(ft.Text("Servicios: 85", color="white"), padding=20, bgcolor="#2a2a3d")),
                    ft.Card(content=ft.Container(ft.Text("Ingresos del mes: $12,450", color="white"), padding=20, bgcolor="#2a2a3d")),
                    ft.Card(content=ft.Container(ft.Text("Eventos activos: 320", color="white"), padding=20, bgcolor="#2a2a3d")),
                ])
            ],
        ),
    )

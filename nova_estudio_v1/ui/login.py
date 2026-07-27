import flet as ft

def login_view(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.add(
        ft.Container(
            bgcolor=ft.colors.GREY_900,
            padding=30,
            border_radius=10,
            content=ft.Column(
                [
                    ft.Text("Inicio de sesión (Admin)", size=20, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                    ft.TextField(label="Correo electrónico", bgcolor=ft.colors.BLACK, color=ft.colors.WHITE, border_color=ft.colors.GREY_600),
                    ft.TextField(label="Contraseña", password=True, bgcolor=ft.colors.BLACK, color=ft.colors.WHITE, border_color=ft.colors.GREY_600),
                    ft.Checkbox(label="Recordarme", check_color=ft.colors.BLACK, fill_color=ft.colors.GREY_300),
                    ft.ElevatedButton("Iniciar sesión", bgcolor=ft.colors.GREY_600, color=ft.colors.BLACK),
                ],
                spacing=15,
            ),
        )
    )

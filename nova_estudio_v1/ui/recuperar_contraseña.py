import flet as ft

def recuperar_view(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.add(
        ft.Container(
            bgcolor=ft.colors.GREY_900,
            padding=30,
            border_radius=10,
            content=ft.Column(
                [
                    ft.Text("Recuperar contraseña", size=20, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                    ft.TextField(label="Correo electrónico", bgcolor=ft.colors.BLACK, color=ft.colors.WHITE, border_color=ft.colors.GREY_600),
                    ft.ElevatedButton("Enviar instrucciones", bgcolor=ft.colors.GREY_600, color=ft.colors.BLACK),
                ],
                spacing=15,
            ),
        )
    )


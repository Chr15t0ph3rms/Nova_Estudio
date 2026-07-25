import flet as ft

def login_view(page: ft.Page):
    return ft.Container(
        expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Iniciar Sesión", size=30, weight=ft.FontWeight.BOLD),
                ft.TextField(label="Correo electrónico", width=300),
                ft.TextField(label="Contraseña", password=True, width=300),
                ft.ElevatedButton(text="Entrar", on_click=lambda e: page.go("/dashboard_usuario")),
                ft.TextButton(text="¿No tienes cuenta? Regístrate aquí", on_click=lambda e: page.go("/registro")),
            ],
        ),
    )

import flet as ft
from ui.inisio_sesion_u import inicio_sesion_u
from ui.admin.dashboard_admin import dashboard_admin

def main(page: ft.Page):
    
    page.title = "DJ Staff Nova Studio"
    page.bgcolor = ft.Colors.BLACK
    page.window_width = 900
    page.window_height = 600
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Widget container
    contenido = ft.Container(
        padding = 5,
        expand = True
    )

    def inicio():
        return ft.Column(
            controls = [
                fondo
            ],
            spacing = 10
        )

    def mostrar_inicio(e = None):
        contenido.content = inicio()
        page.update()

    def inicio_u(e = None):
        contenido.content = inicio_sesion_u(mostrar_inicio)
        page.update()

    fondo = ft.Container(
        image=ft.DecorationImage(
            src="tu_imagen_fondo.jpg",
            fit=ft.BoxFit.COVER,
        ),
        expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    "DJ Staff Nova Studio",
                    size=40,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),
                ft.Text(
                    "Tu música, tu experiencia inolvidable",
                    size=18,
                    color=ft.Colors.WHITE70,
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=40,
                    controls=[
                        # Panel Usuario
                        ft.Container(
                            width=250,
                            height=300,
                            bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                            border_radius=10,
                            padding=20,
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Icon(ft.Icons.PERSON, size=60, color=ft.Colors.WHITE),
                                    ft.Text("Usuario", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                    ft.Text(
                                        "Accede para solicitar eventos,\nver DJs y gestionar tus contrataciones",
                                        color=ft.Colors.WHITE70,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.ElevatedButton(
                                        "Entrar como usuario",
                                        bgcolor=ft.Colors.GREY_700,
                                        color=ft.Colors.WHITE,
                                    ),
                                ],
                            ),
                        ),
                        # Panel Administrador
                        ft.Container(
                            width=250,
                            height=300,
                            bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                            border_radius=10,
                            padding=20,
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Icon(ft.Icons.ADMIN_PANEL_SETTINGS, size=60, color=ft.Colors.WHITE),
                                    ft.Text("Administrador", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                    ft.Text(
                                        "Accede al panel de administrador\npara gestionar la agencia",
                                        color=ft.Colors.WHITE70,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.ElevatedButton(
                                        "Entrar como administrador",
                                        bgcolor=ft.Colors.GREY_700,
                                        color=ft.Colors.WHITE,
                                        on_click = inicio_u
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    layout = ft.Row(
        controls = [
            contenido
        ],
        expand = True
    )

    page.add(layout) # Sin el page.add no se mostraria nada

    mostrar_inicio()
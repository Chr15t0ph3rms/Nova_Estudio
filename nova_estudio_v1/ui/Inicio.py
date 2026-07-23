import flet as ft

def main(page: ft.Page):
    page.title = "DJ Staff Nova Studio"
    page.bgcolor = ft.Colors.BLACK
    page.window_width = 900
    page.window_height = 600
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

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
                                    ft.Icon(ft.icons.PERSON, size=60, color=ft.Colors.WHITE),
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
                                    ft.Icon(ft.icons.ADMIN_PANEL_SETTINGS, size=60, color=ft.Colors.WHITE),
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
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    page.add(fondo)

if __name__ == "__main__":
    ft.app(target=main)

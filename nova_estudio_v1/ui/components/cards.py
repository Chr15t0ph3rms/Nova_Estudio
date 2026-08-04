import flet as ft


def card(titulo, valor, icono):
    return ft.Container(
        width=180,

        height=110,

        bgcolor=ft.Colors.GREY_900,

        border_radius=15,

        padding=15,

        border=ft.Border.all(
            1,

            ft.Colors.GREY_800
        ),

        content=ft.Column(
            [
                ft.Icon(
                    icono,

                    color=ft.Colors.WHITE,

                    size=28
                ),

                ft.Text(
                    str(valor),

                    size=26,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.WHITE
                ),

                ft.Text(
                    titulo,

                    color=ft.Colors.GREY_400,

                    size=14
                )
            ],

            alignment=ft.MainAxisAlignment.CENTER,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            spacing=5
        )
    )

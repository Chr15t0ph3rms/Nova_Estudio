import flet as ft

from dao.cliente_dao import ClienteDAO
from dao.eventos_dao import EventosDAO


def color_por_estado(estado):
    estado = (estado or "").lower()

    if estado == "concretado":
        return ft.Colors.GREEN
    if estado == "cancelado":
        return ft.Colors.RED
    return ft.Colors.AMBER  # "en proceso" u otro valor


def mis_eventos(page: ft.Page, usuario=None):

    contenedor = ft.Container(expand=True)
    eventos_dao = EventosDAO()

    def cargar():

        if not usuario:
            contenedor.content = mensaje("No se encontró tu sesión. Vuelve a iniciar sesión.")
            return

        perfil_cliente = ClienteDAO.obtener_por_usuario(usuario["id"])

        if perfil_cliente is None:
            contenedor.content = mensaje("Tu cuenta todavía no tiene un perfil de cliente vinculado.")
            return

        id_cliente = perfil_cliente[0]
        lista_eventos = eventos_dao.obtener_por_cliente(id_cliente)

        if not lista_eventos:
            contenedor.content = ft.Container(
                expand=True,
                padding=25,
                content=ft.Column(
                    [
                        encabezado(),
                        ft.Text("Aún no tienes eventos. Renta un paquete para crear uno.", color=ft.Colors.WHITE70),
                    ],
                    expand=True,
                ),
            )
            return

        tarjetas = [tarjeta_evento(ev, id_cliente) for ev in lista_eventos]

        contenedor.content = ft.Container(
            expand=True,
            padding=25,
            content=ft.Column(
                [
                    encabezado(),
                    ft.Container(height=10),
                    ft.Column(tarjetas, spacing=15, scroll=ft.ScrollMode.AUTO),
                ],
                expand=True,
            ),
        )

    def encabezado():
        return ft.Column(
            [
                ft.Text("Mis Eventos", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text("Aquí puedes ver el estado de tus eventos", size=15, color=ft.Colors.WHITE70),
                ft.Container(height=10),
                ft.Divider(),
            ]
        )

    def mensaje(texto):
        return ft.Container(
            expand=True,
            padding=25,
            content=ft.Column(
                [
                    encabezado(),
                    ft.Text(texto, color=ft.Colors.WHITE70),
                ]
            ),
        )

    def cancelar_evento(id_evento):

        eventos_dao.actualizar_estado(id_evento, "Cancelado")
        cargar()
        page.update()

    def tarjeta_evento(evento, id_cliente):

        color = color_por_estado(evento.estado)

        return ft.Container(
            bgcolor=ft.Colors.GREY_900,
            border=ft.Border.all(1.5, color),
            border_radius=15,
            padding=20,

            content=ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(evento.nombre, size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Text(f"Fecha: {evento.fecha}", color=ft.Colors.WHITE70),
                            ft.Text(f"Costo: ${evento.costo}", color=ft.Colors.WHITE70),
                        ],
                        expand=True,
                        spacing=4,
                    ),

                    ft.Column(
                        [
                            ft.Container(
                                bgcolor=color,
                                border_radius=20,
                                padding=ft.Padding.symmetric(horizontal=14, vertical=6),
                                content=ft.Text(evento.estado, size=12, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                            ),

                            ft.Container(height=8),

                            ft.OutlinedButton(
                                "Cancelar",
                                style=ft.ButtonStyle(color=ft.Colors.RED, side=ft.BorderSide(1, ft.Colors.RED)),
                                on_click=lambda e, id_ev=evento.id_evento: cancelar_evento(id_ev),
                                disabled=(evento.estado != "En proceso"),
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
        )

    cargar()

    return contenedor

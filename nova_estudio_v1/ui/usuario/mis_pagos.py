import flet as ft

from dao.cliente_dao import ClienteDAO
from dao.pago_dao import PagoDAO

def color_por_estado_pago(estado):
    estado = (estado or "").lower()

    if estado == "pagado":
        return ft.Colors.GREEN
    if estado == "cancelado":
        return ft.Colors.RED
    return ft.Colors.AMBER  # "pendiente" u otro valor

def mis_pagos(page: ft.Page, usuario=None):

    if not usuario:
        return mensaje_simple("No se encontró tu sesión. Vuelve a iniciar sesión.")

    perfil_cliente = ClienteDAO.obtener_por_usuario(usuario["id"])

    if perfil_cliente is None:
        return mensaje_simple("Tu cuenta todavía no tiene un perfil de cliente vinculado.")

    id_cliente = perfil_cliente[0]

    dao = PagoDAO()
    lista_pagos = dao.obtener_por_cliente(id_cliente)

    saldo_total = sum(
        float(p.monto) for p in lista_pagos if (p.estado or "").lower() == "pagado"
    )

    if not lista_pagos:
        return ft.Container(
            expand=True,
            padding=25,
            content=ft.Column(
                [
                    encabezado(),
                    ft.Text("Aún no tienes pagos registrados.", color=ft.Colors.WHITE70),
                ]
            ),
        )

    filas = [tarjeta_pago(p) for p in lista_pagos]

    return ft.Container(
        expand=True,
        padding=25,
        content=ft.Column(
            [
                encabezado(),

                ft.Text(f"Total pagado: ${saldo_total}", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),

                ft.Container(height=15),

                ft.Column(filas, spacing=12, scroll=ft.ScrollMode.ALWAYS),
            ],
            expand=True,
        ),
    )

def encabezado():
    return ft.Column(
        [
            ft.Text("Mis Pagos", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ft.Text("Historial de tus pagos realizados", size=15, color=ft.Colors.WHITE70),
            ft.Container(height=10),
            ft.Divider(),
        ]
    )

def mensaje_simple(texto):
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

def tarjeta_pago(pago):

    color = color_por_estado_pago(pago.estado)

    return ft.Container(
        bgcolor=ft.Colors.GREY_900,
        border=ft.Border.all(1.5, color),
        border_radius=12,
        padding=18,

        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text(f"${pago.monto}", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(f"Fecha: {pago.fecha_pago}", size=13, color=ft.Colors.WHITE70),
                    ],
                    spacing=2,
                ),

                ft.Container(
                    bgcolor=color,
                    border_radius=20,
                    padding=ft.Padding.symmetric(horizontal=14, vertical=6),
                    content=ft.Text(pago.estado, size=12, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )

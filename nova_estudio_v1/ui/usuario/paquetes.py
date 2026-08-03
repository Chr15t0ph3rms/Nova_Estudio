import flet as ft
import datetime

from dao.paquetes_dao import PaquetesDAO
from dao.cliente_dao import ClienteDAO
from dao.eventos_dao import EventosDAO
from modelos.eventos import Eventos


def color_por_paquete(nombre):
    nombre = (nombre or "").lower()

    if "oro" in nombre:
        return ft.Colors.AMBER
    if "plata" in nombre:
        return ft.Colors.BLUE_GREY_200
    if "bronce" in nombre:
        return ft.Colors.ORANGE
    if "cobre" in nombre:
        return ft.Colors.DEEP_ORANGE_300
    if "diamante" in nombre:
        return ft.Colors.CYAN_ACCENT_200
    if "neon" in nombre or "neón" in nombre:
        return ft.Colors.PINK_300

    return ft.Colors.PURPLE_200


def paquetes(page: ft.Page, usuario=None):

    dao = PaquetesDAO()
    contenedor = ft.Container(expand=True)

    # ==========================
    # PANTALLA 1: LISTA DE PAQUETES
    # ==========================

    def mostrar_lista():

        lista_paquetes = dao.obtener_todo()

        if not lista_paquetes:
            tarjetas = [ft.Text("Aún no hay paquetes disponibles.", color=ft.Colors.WHITE70)]
        else:
            tarjetas = [tarjeta_paquete(p) for p in lista_paquetes]

        contenedor.content = ft.Container(
            expand=True,
            padding=25,
            content=ft.Column(
                [
                    ft.Text("Paquetes Disponibles", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text("Elige el paquete ideal para tu evento", size=15, color=ft.Colors.WHITE70),
                    ft.Container(height=10),
                    ft.Divider(),
                    ft.Container(height=10),
                    ft.Row(tarjetas, wrap=True, spacing=20, run_spacing=20),
                ],
                expand=True,
                scroll=ft.ScrollMode.AUTO,
            ),
        )

        page.update()

    def mostrar_detalles(paquete, color):

        caracteristicas = [i.strip() for i in (paquete.descripcion or "").split(",") if i.strip()]

        page.show_dialog(
            ft.AlertDialog(
                title=ft.Text(paquete.nombre.upper(), color=color, weight=ft.FontWeight.BOLD),
                content=ft.Column(
                    [
                        ft.Text(paquete.tipo_paquete, color=ft.Colors.WHITE70),
                        ft.Text(f"Costo: ${paquete.costo}", size=20, weight=ft.FontWeight.BOLD),
                        ft.Divider(),
                        *[
                            ft.Row(
                                [ft.Icon(ft.Icons.CHECK_CIRCLE, size=16, color=color), ft.Text(i)],
                                spacing=8,
                            )
                            for i in caracteristicas
                        ],
                    ],
                    tight=True,
                    spacing=8,
                ),
            )
        )

    def tarjeta_paquete(paquete):

        color = color_por_paquete(paquete.nombre)
        caracteristicas = [i.strip() for i in (paquete.descripcion or "").split(",") if i.strip()]

        return ft.Container(
            width=250,
            bgcolor=ft.Colors.GREY_900,
            border=ft.Border.all(1.5, color),
            border_radius=15,
            padding=20,

            content=ft.Column(
                [
                    ft.Text(paquete.nombre.upper(), size=16, weight=ft.FontWeight.BOLD, color=color),
                    ft.Text(paquete.tipo_paquete, size=13, color=ft.Colors.WHITE70),
                    ft.Container(height=8),
                    ft.Text(f"${paquete.costo}", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Container(height=10),

                    ft.Column(
                        [
                            ft.Row(
                                [ft.Icon(ft.Icons.CHECK_CIRCLE, size=16, color=color), ft.Text(i, size=13, color=ft.Colors.WHITE70)],
                                spacing=8,
                            )
                            for i in caracteristicas
                        ],
                        spacing=6,
                    ),

                    ft.Container(height=15),

                    ft.OutlinedButton(
                        "Ver detalles",
                        style=ft.ButtonStyle(color=color, side=ft.BorderSide(1, color)),
                        width=200,
                        on_click=lambda e, p=paquete, c=color: mostrar_detalles(p, c),
                    ),

                    ft.Container(height=8),

                    ft.ElevatedButton(
                        "Rentar",
                        bgcolor=color,
                        color=ft.Colors.BLACK,
                        width=200,
                        on_click=lambda e, p=paquete, c=color: mostrar_confirmacion(p, c),
                    ),
                ],
                spacing=4,
            ),
        )

    # ==========================
    # PANTALLA 2: CONFIRMAR RENTA
    # ==========================

    def mostrar_confirmacion(paquete, color):

        contenedor.content = ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0),

            content=ft.Container(
                width=420,
                bgcolor=ft.Colors.GREY_900,
                border=ft.Border.all(1.5, color),
                border_radius=15,
                padding=30,

                content=ft.Column(
                    [
                        ft.Text("Confirmar renta", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Divider(),

                        ft.Text(f"Paquete: {paquete.nombre}", size=16, color=ft.Colors.WHITE),
                        ft.Text(f"Tipo: {paquete.tipo_paquete}", color=ft.Colors.WHITE70),
                        ft.Text(f"Costo total: ${paquete.costo}", size=20, weight=ft.FontWeight.BOLD, color=color),

                        ft.Container(height=15),
                        ft.Text("¿Confirmas que quieres rentar este paquete?", color=ft.Colors.WHITE70),
                        ft.Container(height=15),

                        ft.Row(
                            [
                                ft.OutlinedButton("Cancelar", on_click=lambda e: mostrar_lista()),
                                ft.ElevatedButton(
                                    "Confirmar",
                                    bgcolor=color,
                                    color=ft.Colors.BLACK,
                                    on_click=lambda e, p=paquete, c=color: mostrar_pago(p, c),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=15,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                ),
            ),
        )

        page.update()

    # ==========================
    # PANTALLA 3: FORMULARIO DE PAGO
    # ==========================

    def mostrar_pago(paquete, color):

        nombre_titular = ft.TextField(
            label="Nombre del titular de la tarjeta",
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
        )

        numero_tarjeta = ft.TextField(
            label="Número de la tarjeta",
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
            max_length=19,
        )

        mes_vencimiento = ft.Dropdown(
            label="Mes de vencimiento",
            options=[ft.dropdown.Option(f"{m:02d}") for m in range(1, 13)],
            width=150,
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
        )

        anio_actual = datetime.date.today().year
        anio_vencimiento = ft.Dropdown(
            label="Año de vencimiento",
            options=[ft.dropdown.Option(str(anio_actual + i)) for i in range(0, 11)],
            width=150,
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
        )

        cvv = ft.TextField(
            label="CVV",
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
            password=True,
            can_reveal_password=True,
            max_length=4,
            width=150,
        )

        def procesar_pago(e):

            # Validación básica de formato (nada de esto se guarda en la BD)
            if not nombre_titular.value.strip():
                page.show_dialog(ft.AlertDialog(title=ft.Text("Falta el nombre del titular")))
                return

            numero_limpio = numero_tarjeta.value.replace(" ", "")
            if not numero_limpio.isdigit() or len(numero_limpio) < 13:
                page.show_dialog(ft.AlertDialog(title=ft.Text("Número de tarjeta inválido")))
                return

            if not mes_vencimiento.value or not anio_vencimiento.value:
                page.show_dialog(ft.AlertDialog(title=ft.Text("Falta la fecha de vencimiento")))
                return

            if not cvv.value or not cvv.value.isdigit() or len(cvv.value) < 3:
                page.show_dialog(ft.AlertDialog(title=ft.Text("CVV inválido")))
                return

            # Crear el evento real, ligado a este cliente, con estado "En proceso"
            perfil_cliente = ClienteDAO.obtener_por_usuario(usuario["id"]) if usuario else None

            if perfil_cliente is None:
                page.show_dialog(
                    ft.AlertDialog(
                        title=ft.Text("No se pudo crear el evento"),
                        content=ft.Text("Tu cuenta no tiene un perfil de cliente vinculado todavía."),
                    )
                )
                return

            id_cliente, telefono, calle, numero_exterior, colonia = perfil_cliente

            eventos_dao = EventosDAO()
            nuevo_id = eventos_dao.obtener_ultimo_id() + 1

            nuevo_evento = Eventos(
                id_evento=nuevo_id,
                nombre=f"Evento - Paquete {paquete.nombre}",
                fecha=datetime.date.today(),
                hora=datetime.datetime.now().time(),
                calle=calle,
                colonia=colonia,
                numero_exterior=numero_exterior,
                costo=paquete.costo,
                id_cliente=id_cliente,
                estado="En proceso",
            )

            eventos_dao.insertar(nuevo_evento)

            page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("¡Renta confirmada!"),
                    content=ft.Text(f"Rentaste el paquete '{paquete.nombre}' por ${paquete.costo}. Ya puedes verlo en 'Mis Eventos'."),
                )
            )

            mostrar_lista()

        contenedor.content = ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0),

            content=ft.Container(
                width=480,
                bgcolor=ft.Colors.GREY_900,
                border=ft.Border.all(1.5, color),
                border_radius=15,
                padding=30,

                content=ft.Column(
                    [
                        ft.Text(
                            "Agregar una tarjeta de crédito o débito",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE,
                            text_align=ft.TextAlign.CENTER,
                        ),

                        ft.Divider(),

                        ft.Text("Todos los campos son obligatorios", size=12, color=ft.Colors.WHITE70),

                        ft.Row(
                            [
                                ft.Icon(ft.Icons.CREDIT_CARD, color=ft.Colors.WHITE70),
                                ft.Text("Se aceptan Visa, Mastercard y Amex", size=12, color=ft.Colors.WHITE70),
                            ],
                            spacing=8,
                        ),

                        ft.Container(height=10),

                        nombre_titular,
                        numero_tarjeta,

                        ft.Row([mes_vencimiento, anio_vencimiento, cvv], spacing=10),

                        ft.Row(
                            [
                                ft.Icon(ft.Icons.HELP_OUTLINE, size=16, color=ft.Colors.WHITE70),
                                ft.Text(
                                    "¿Dónde encuentro el CVV? Últimos 3 dígitos de la parte trasera.",
                                    size=12,
                                    color=ft.Colors.WHITE70,
                                ),
                            ],
                            spacing=6,
                        ),

                        ft.Container(height=15),

                        ft.Row(
                            [
                                ft.OutlinedButton("Atrás", on_click=lambda e: mostrar_confirmacion(paquete, color)),
                                ft.ElevatedButton(
                                    "Siguiente",
                                    bgcolor=color,
                                    color=ft.Colors.BLACK,
                                    on_click=procesar_pago,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=15,
                        ),
                    ],
                    spacing=8,
                ),
            ),
        )

        page.update()

    mostrar_lista()

    return contenedor

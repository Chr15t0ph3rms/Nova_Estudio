import flet as ft
import datetime

from dao.paquetes_dao import PaquetesDAO
from dao.cliente_dao import ClienteDAO
from dao.eventos_dao import EventosDAO
from dao.pago_dao import PagoDAO
from modelos.eventos import Eventos
from modelos.pago import Pago

# Salones disponibles por municipio (datos de ejemplo)
MUNICIPIOS_SALONES = {
    "Apizaco": ["Salón Jardín Apizaco", "Salón Los Pinos", "Terraza Apizaco Eventos"],
    "Huamantla": ["Salón Hacienda Huamantla", "Jardín San Miguel", "Salón Real Huamantla"],
    "Tlaxcala": ["Salón Centro Tlaxcala", "Jardín Xicohténcatl", "Hacienda Tlaxcala"],
    "Chiautempan": ["Salón Los Encinos", "Jardín Chiautempan"],
    "Zacatelco": ["Salón Zacatelco Eventos", "Jardín San Esteban"],
}

TIPOS_EVENTO = ["Boda", "XV años", "Cumpleaños", "Fiesta infantil"]

def imagen_por_paquete(nombre):
    nombre = (nombre or "").lower()

    if "oro" in nombre:
        return "paquete_oro.jpg"
    if "plata" in nombre:
        return "paquete_plata.jpg"
    if "cobre" in nombre:
        return "paquete_cobre.jpg"
    if "diamante" in nombre:
        return "paquete_diamante.jpg"
    if "bronce" in nombre:
        return "paquete_bronce.jpg"
    if "neon" in nombre or "neón" in nombre:
        return "paquete_neon.jpg"
    if "audio" in nombre:
        return "renta_audio.jpg"

    return "paquete_generico.jpg"

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
    if "audio" in nombre:
        return ft.Colors.BLUE_400

    return ft.Colors.PURPLE_200

def paquetes(page: ft.Page, usuario=None):

    dao = PaquetesDAO()
    contenedor = ft.Container(expand=True)

    # Pantalla 1: lista de paquetes

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
                scroll=ft.ScrollMode.ALWAYS,
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
            height=530,
            bgcolor=ft.Colors.GREY_900,
            border=ft.Border.all(1.5, color),
            border_radius=15,
            padding=20,

            content=ft.Column(
                [
                    ft.Container(
                        height=110,
                        border_radius=10,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        content=ft.Image(
                            src=imagen_por_paquete(paquete.nombre),
                            fit=ft.BoxFit.COVER,
                            width=float("inf"),
                            height=110,
                        ),
                    ),

                    ft.Container(height=10),

                    ft.Text(
                        paquete.nombre.upper(),
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=color,
                        max_lines=1,
                        overflow=ft.TextOverflow.ELLIPSIS,
                    ),
                    ft.Text(
                        paquete.tipo_paquete,
                        size=13,
                        color=ft.Colors.WHITE70,
                        max_lines=1,
                        overflow=ft.TextOverflow.ELLIPSIS,
                    ),
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

                    # Espaciador flexible: empuja siempre los botones hasta el
                    # fondo de la tarjeta, sin importar cuántas
                    # características tenga cada paquete.
                    ft.Container(expand=True),

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
                expand=True,
            ),
        )

    # Pantalla 2: confirmar renta

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

                        ft.Column(
                            [
                                ft.ElevatedButton(
                                    "Confirmar",
                                    bgcolor=color,
                                    color=ft.Colors.BLACK,
                                    width=250,
                                    on_click=lambda e, p=paquete, c=color: mostrar_metodo_pago(p, c),
                                ),
                                ft.OutlinedButton(
                                    "Cancelar",
                                    style=ft.ButtonStyle(color=ft.Colors.RED, side=ft.BorderSide(1, ft.Colors.RED)),
                                    width=250,
                                    on_click=lambda e: mostrar_lista(),
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                ),
            ),
        )

        page.update()

    # Pantalla 2.5: elegir método de pago

    def mostrar_metodo_pago(paquete, color):

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
                        ft.Text("¿Cómo quieres pagar?", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Divider(),

                        ft.Text(f"Paquete: {paquete.nombre} — ${paquete.costo}", color=ft.Colors.WHITE70),

                        ft.Container(height=15),

                        ft.ElevatedButton(
                            "Tarjeta de crédito o débito",
                            icon=ft.Icons.CREDIT_CARD,
                            bgcolor=color,
                            color=ft.Colors.BLACK,
                            width=300,
                            on_click=lambda e, p=paquete, c=color: mostrar_pago(p, c),
                        ),

                        ft.Container(height=10),

                        ft.OutlinedButton(
                            "Pago en efectivo",
                            icon=ft.Icons.PAYMENTS_OUTLINED,
                            style=ft.ButtonStyle(color=color, side=ft.BorderSide(1, color)),
                            width=300,
                            on_click=lambda e, p=paquete, c=color: mostrar_orden_efectivo(p, c),
                        ),

                        ft.Container(height=15),

                        ft.TextButton("Regresar", on_click=lambda e, p=paquete, c=color: mostrar_confirmacion(p, c)),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                ),
            ),
        )

        page.update()

    # Pantalla 2.6: orden de pago en efectivo

    def mostrar_orden_efectivo(paquete, color):

        nombre_contrata = ft.TextField(
            label="Nombre de quien contrata",
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
        )

        municipio = ft.Dropdown(
            label="Municipio",
            options=[ft.dropdown.Option(m) for m in MUNICIPIOS_SALONES.keys()],
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
        )

        salon = ft.TextField(
            label="Ubicación",
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
        )

        tipo_evento = ft.Dropdown(
            label="Tipo de evento",
            options=[ft.dropdown.Option(t) for t in TIPOS_EVENTO],
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
        )

        def generar_orden(e):

            if not nombre_contrata.value.strip():
                page.show_dialog(ft.AlertDialog(title=ft.Text("Falta el nombre de quien contrata")))
                return

            if not municipio.value:
                page.show_dialog(ft.AlertDialog(title=ft.Text("Falta elegir el municipio")))
                return

            if not salon.value.strip():
                page.show_dialog(ft.AlertDialog(title=ft.Text("Falta la ubicación")))
                return

            if not tipo_evento.value:
                page.show_dialog(ft.AlertDialog(title=ft.Text("Falta elegir el tipo de evento")))
                return

            mostrar_recibo(
                paquete=paquete,
                color=color,
                nombre_contrata=nombre_contrata.value,
                municipio_val=municipio.value,
                ubicacion_val=salon.value,
                tipo_evento_val=tipo_evento.value,
            )

        contenedor.content = ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0),

            content=ft.Container(
                width=460,
                bgcolor=ft.Colors.GREY_900,
                border=ft.Border.all(1.5, color),
                border_radius=15,
                padding=30,

                content=ft.Column(
                    [
                        ft.Text("Orden de pago en efectivo", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Divider(),

                        ft.Text(f"Paquete: {paquete.nombre} — ${paquete.costo}", color=ft.Colors.WHITE70),
                        ft.Container(height=10),

                        nombre_contrata,
                        municipio,
                        salon,
                        tipo_evento,

                        ft.Container(height=15),

                        ft.Column(
                            [
                                ft.ElevatedButton(
                                    "Generar orden de pago",
                                    bgcolor=color,
                                    color=ft.Colors.BLACK,
                                    width=280,
                                    on_click=generar_orden,
                                ),
                                ft.OutlinedButton(
                                    "Atrás",
                                    width=280,
                                    on_click=lambda e: mostrar_metodo_pago(paquete, color),
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                        ),
                    ],
                    spacing=8,
                    scroll=ft.ScrollMode.ALWAYS,
                ),
            ),
        )

        page.update()

    # Pantalla 2.7: recibo / orden de pago visual

    def mostrar_recibo(paquete, color, nombre_contrata, municipio_val, ubicacion_val, tipo_evento_val):

        eventos_dao = EventosDAO()
        folio = f"NS-{datetime.date.today().year}-{eventos_dao.obtener_ultimo_id() + 1:04d}"

        perfil_cliente = ClienteDAO.obtener_por_usuario(usuario["id"]) if usuario else None
        telefono = perfil_cliente[1] if perfil_cliente else "—"
        correo = usuario.get("correo", "—") if usuario else "—"

        def fila(etiqueta, valor):
            return ft.Row(
                [
                    ft.Text(etiqueta, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, width=110),
                    ft.Text(str(valor), color=ft.Colors.BLACK, expand=True),
                ],
            )

        def seccion(titulo, contenido):
            return ft.Container(
                border=ft.Border.all(1, ft.Colors.GREY_400),
                border_radius=8,
                padding=15,
                content=ft.Column(
                    [
                        ft.Container(
                            bgcolor=ft.Colors.BLACK,
                            padding=8,
                            border_radius=6,
                            content=ft.Text(titulo, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD, size=13),
                        ),
                        ft.Container(height=6),
                        *contenido,
                    ],
                    spacing=4,
                ),
            )

        def cancelar(e):
            mostrar_orden_efectivo(paquete, color)

        def aceptar(e):

            if perfil_cliente is None:
                page.show_dialog(
                    ft.AlertDialog(
                        title=ft.Text("No se pudo registrar el pago"),
                        content=ft.Text("Tu cuenta no tiene un perfil de cliente vinculado todavía."),
                    )
                )
                return

            id_cliente = perfil_cliente[0]

            nuevo_id_evento = eventos_dao.obtener_ultimo_id() + 1

            nuevo_evento = Eventos(
                id_evento=nuevo_id_evento,
                nombre=f"{tipo_evento_val} - Paquete {paquete.nombre}",
                fecha=datetime.date.today(),
                hora=datetime.datetime.now().time(),
                calle=ubicacion_val,
                colonia=municipio_val,
                numero_exterior=0,
                costo=paquete.costo,
                id_cliente=id_cliente,
                estado="En proceso",
            )

            eventos_dao.insertar(nuevo_evento)

            pago_dao = PagoDAO()
            nuevo_id_pago = pago_dao.obtener_ultimo_id() + 1

            nuevo_pago = Pago(
                id_pago=nuevo_id_pago,
                id_contrato=None,
                fecha_pago=datetime.date.today(),
                monto=paquete.costo,
                estado="Pagado",
                id_cliente=id_cliente,
                id_evento=nuevo_id_evento,
            )

            pago_dao.insertar(nuevo_pago)

            page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("¡Pago concretado!"),
                    content=ft.Text(f"Ya puedes ver tu evento y tu pago en 'Mis Eventos' y 'Mis Pagos'."),
                )
            )

            mostrar_lista()

        recibo = ft.Container(
            width=480,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,

            content=ft.Column(
                [
                    # ENCABEZADO
                    ft.Container(
                        bgcolor=ft.Colors.BLACK,
                        padding=20,
                        content=ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Text("NOVA STUDIO", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                        ft.Text("ORDEN DE PAGO", size=18, weight=ft.FontWeight.BOLD, color=color),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                ft.Text("Agencia de DJs y producción de eventos", size=11, color=ft.Colors.WHITE70),
                                ft.Container(height=6),
                                ft.Text(f"Folio: {folio}", size=12, color=color, weight=ft.FontWeight.BOLD),
                            ],
                            spacing=2,
                        ),
                    ),

                    ft.Container(
                        padding=20,
                        content=ft.Column(
                            [
                                seccion(
                                    "DATOS DEL CLIENTE",
                                    [
                                        fila("Nombre:", nombre_contrata),
                                        fila("Teléfono:", telefono),
                                        fila("Correo:", correo),
                                    ],
                                ),

                                ft.Container(height=12),

                                seccion(
                                    "DATOS DEL EVENTO",
                                    [
                                        fila("Concepto:", tipo_evento_val),
                                        fila("Fecha:", datetime.date.today().strftime("%d/%m/%Y")),
                                        fila("Lugar:", f"{ubicacion_val}, {municipio_val}"),
                                    ],
                                ),

                                ft.Container(height=12),

                                seccion(
                                    "SERVICIO",
                                    [
                                        ft.Row(
                                            [
                                                ft.Text("Descripción", weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, expand=True),
                                                ft.Text("Importe", weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                                            ]
                                        ),
                                        ft.Divider(height=1),
                                        ft.Row(
                                            [
                                                ft.Text(f"Paquete {paquete.nombre}", color=ft.Colors.BLACK, expand=True),
                                                ft.Text(f"${paquete.costo}", color=ft.Colors.BLACK),
                                            ]
                                        ),
                                    ],
                                ),

                                ft.Container(height=12),

                                ft.Container(
                                    bgcolor=color,
                                    border_radius=8,
                                    padding=12,
                                    content=ft.Row(
                                        [
                                            ft.Text("TOTAL A PAGAR", weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                                            ft.Text(f"${paquete.costo} MXN", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    ),
                                ),

                                ft.Container(height=12),

                                ft.Container(
                                    border=ft.Border.all(1, ft.Colors.AMBER),
                                    border_radius=8,
                                    padding=12,
                                    content=ft.Column(
                                        [
                                            ft.Text("Observaciones", weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, size=12),
                                            ft.Text("• Pago en efectivo al confirmar el evento.", color=ft.Colors.BLACK, size=12),
                                            ft.Text("• Presenta este folio el día del evento.", color=ft.Colors.BLACK, size=12),
                                            ft.Text("• En caso de cancelación, consulta política de reembolso.", color=ft.Colors.BLACK, size=12),
                                        ],
                                        spacing=4,
                                    ),
                                ),

                                ft.Container(height=15),

                                ft.Column(
                                    [
                                        ft.ElevatedButton(
                                            "Aceptar",
                                            bgcolor=ft.Colors.GREEN,
                                            color=ft.Colors.WHITE,
                                            width=300,
                                            on_click=aceptar,
                                        ),
                                        ft.OutlinedButton(
                                            "Cancelar",
                                            style=ft.ButtonStyle(color=ft.Colors.RED, side=ft.BorderSide(1, ft.Colors.RED)),
                                            width=300,
                                            on_click=cancelar,
                                        ),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=10,
                                ),
                            ],
                            spacing=4,
                        ),
                    ),
                ],
                spacing=0,
            ),
        )

        contenedor.content = ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0),
            padding=20,
            content=ft.Column(
                [recibo],
                scroll=ft.ScrollMode.ALWAYS,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

        page.update()

    # Pantalla 3: datos del evento (antes de la tarjeta)

    def mostrar_pago(paquete, color):

        nombre_contrata = ft.TextField(
            label="Nombre de quien contrata",
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
        )

        municipio = ft.Dropdown(
            label="Municipio",
            options=[ft.dropdown.Option(m) for m in MUNICIPIOS_SALONES.keys()],
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
        )

        salon = ft.TextField(
            label="Ubicación",
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
        )

        tipo_evento = ft.Dropdown(
            label="Tipo de evento",
            options=[ft.dropdown.Option(t) for t in TIPOS_EVENTO],
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
        )

        def continuar(e):

            if not nombre_contrata.value.strip():
                page.show_dialog(ft.AlertDialog(title=ft.Text("Falta el nombre de quien contrata")))
                return

            if not municipio.value:
                page.show_dialog(ft.AlertDialog(title=ft.Text("Falta elegir el municipio")))
                return

            if not salon.value.strip():
                page.show_dialog(ft.AlertDialog(title=ft.Text("Falta la ubicación")))
                return

            if not tipo_evento.value:
                page.show_dialog(ft.AlertDialog(title=ft.Text("Falta elegir el tipo de evento")))
                return

            mostrar_formulario_tarjeta(
                paquete=paquete,
                color=color,
                nombre_contrata=nombre_contrata.value,
                municipio_val=municipio.value,
                ubicacion_val=salon.value,
                tipo_evento_val=tipo_evento.value,
            )

        contenedor.content = ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0),

            content=ft.Container(
                width=460,
                bgcolor=ft.Colors.GREY_900,
                border=ft.Border.all(1.5, color),
                border_radius=15,
                padding=30,

                content=ft.Column(
                    [
                        ft.Text("Datos del evento", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Divider(),

                        ft.Text(f"Paquete: {paquete.nombre} — ${paquete.costo}", color=ft.Colors.WHITE70),
                        ft.Container(height=10),

                        nombre_contrata,
                        municipio,
                        salon,
                        tipo_evento,

                        ft.Container(height=15),

                        ft.Column(
                            [
                                ft.ElevatedButton(
                                    "Continuar",
                                    bgcolor=color,
                                    color=ft.Colors.BLACK,
                                    width=250,
                                    on_click=continuar,
                                ),
                                ft.OutlinedButton(
                                    "Cancelar",
                                    style=ft.ButtonStyle(color=ft.Colors.RED, side=ft.BorderSide(1, ft.Colors.RED)),
                                    width=250,
                                    on_click=lambda e: mostrar_lista(),
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                        ),
                    ],
                    spacing=8,
                    scroll=ft.ScrollMode.ALWAYS,
                ),
            ),
        )

        page.update()

    # Pantalla 3.5: formulario de tarjeta

    def mostrar_formulario_tarjeta(paquete, color, nombre_contrata, municipio_val, ubicacion_val, tipo_evento_val):

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

            id_cliente = perfil_cliente[0]

            eventos_dao = EventosDAO()
            nuevo_id = eventos_dao.obtener_ultimo_id() + 1

            nuevo_evento = Eventos(
                id_evento=nuevo_id,
                nombre=f"{tipo_evento_val} - Paquete {paquete.nombre}",
                fecha=datetime.date.today(),
                hora=datetime.datetime.now().time(),
                calle=ubicacion_val,
                colonia=municipio_val,
                numero_exterior=0,
                costo=paquete.costo,
                id_cliente=id_cliente,
                estado="En proceso",
            )

            eventos_dao.insertar(nuevo_evento)

            # Registrar el pago de este paquete, ligado al cliente y al evento recién creado
            pago_dao = PagoDAO()
            nuevo_id_pago = pago_dao.obtener_ultimo_id() + 1

            nuevo_pago = Pago(
                id_pago=nuevo_id_pago,
                id_contrato=None,
                fecha_pago=datetime.date.today(),
                monto=paquete.costo,
                estado="Pagado",
                id_cliente=id_cliente,
                id_evento=nuevo_id,
            )

            pago_dao.insertar(nuevo_pago)

            page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("¡Renta confirmada!"),
                    content=ft.Text(f"Rentaste el paquete '{paquete.nombre}' por ${paquete.costo}. Ya puedes verlo en 'Mis Eventos' y 'Mis Pagos'."),
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

                        ft.Column(
                            [
                                ft.ElevatedButton(
                                    "Siguiente",
                                    bgcolor=color,
                                    color=ft.Colors.BLACK,
                                    width=280,
                                    on_click=procesar_pago,
                                ),
                                ft.OutlinedButton(
                                    "Atrás",
                                    width=280,
                                    on_click=lambda e: mostrar_pago(paquete, color),
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                        ),
                    ],
                    spacing=8,
                    scroll=ft.ScrollMode.ALWAYS,
                ),
            ),
        )

        page.update()

    mostrar_lista()

    return contenedor

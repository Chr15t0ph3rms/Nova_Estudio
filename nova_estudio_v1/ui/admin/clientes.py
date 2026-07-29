import flet as ft

from dao.cliente_dao import ClienteDAO
from modelos.cliente import Cliente


def clientes(page: ft.Page):

    cliente_dao = ClienteDAO()
    cliente_seleccionado = None

    # CAMPOS

    txt_nombre = ft.TextField(
        label="Nombre",
        width=250
    )

    txt_app = ft.TextField(
        label="Apellido Paterno",
        width=250
    )

    txt_apm = ft.TextField(
        label="Apellido Materno",
        width=250
    )

    txt_telefono = ft.TextField(
        label="Teléfono",
        width=250
    )

    txt_correo = ft.TextField(
        label="Correo",
        width=250
    )

    txt_calle = ft.TextField(
        label="Calle",
        width=250
    )

    txt_numero_exterior = ft.TextField(
        label="Número Exterior",
        width=250
    )

    txt_colonia = ft.TextField(
        label="Colonia",
        width=250
    )

    txt_buscar = ft.TextField(
        label="Buscar cliente",
        prefix_icon=ft.Icons.SEARCH,
        expand=True
    )


    # TABLA DE CLIENTES

    tabla_clientes = ft.DataTable(

        columns=[

            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Teléfono")),
            ft.DataColumn(ft.Text("Correo")),
            ft.DataColumn(ft.Text("Acciones"))

        ],

        rows=[]

    )

    # CARGAR CLIENTES

    def cargar_clientes():

        tabla_clientes.rows.clear()

        try:

            lista_clientes = cliente_dao.obtener_todos()

            for cliente in lista_clientes:

                tabla_clientes.rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(
                                ft.Text(str(cliente.id_cliente))
                            ),

                            ft.DataCell(
                                ft.Text(
                                    f"{cliente.nombre} {cliente.app} {cliente.apm}"
                                )
                            ),

                            ft.DataCell(
                                ft.Text(cliente.telefono)
                            ),

                            ft.DataCell(
                                ft.Text(cliente.correo)
                            ),

                            ft.DataCell(

                                ft.Row(

                                    [

                                        ft.IconButton(
                                            icon=ft.Icons.EDIT,
                                            tooltip="Editar",
                                            on_click=lambda e, c=cliente: editar_cliente(c)
                                        ),

                                        ft.IconButton(
                                            icon=ft.Icons.DELETE,
                                            tooltip="Eliminar",
                                            icon_color=ft.Colors.RED,
                                            on_click=lambda e, c=cliente: eliminar_cliente(c)
                                        )

                                    ]

                                )

                            )

                        ]

                    )

                )

            page.update()


        except Exception as error:

            page.snack_bar = ft.SnackBar(
                ft.Text(
                    f"Error al cargar clientes: {error}"
                )
            )

            page.snack_bar.open = True

            page.update()



    
    # LIMPIAR CAMPOS
    

    def limpiar_campos():

        txt_nombre.value = ""

        txt_app.value = ""

        txt_apm.value = ""

        txt_telefono.value = ""

        txt_correo.value = ""

        txt_calle.value = ""

        txt_numero_exterior.value = ""

        txt_colonia.value = ""

    # GUARDAR CLIENTE


    def guardar_cliente(e):

        try:

            nuevo_id = cliente_dao.obtener_ultimo_id() + 1


            cliente = Cliente(

                nuevo_id,

                txt_nombre.value,

                txt_app.value,

                txt_apm.value,

                txt_telefono.value,

                txt_correo.value,

                txt_calle.value,

                txt_numero_exterior.value,

                txt_colonia.value

            )


            cliente_dao.insertar(cliente)


            cerrar_dialogo()

            limpiar_campos()

            cargar_clientes()


            mostrar_mensaje(
                "Cliente registrado correctamente."
            )


        except Exception as error:

            mostrar_mensaje(
                f"Error al guardar cliente: {error}"
            )




    # EDITAR CLIENTE


    def editar_cliente(cliente):

        nonlocal cliente_seleccionado


        cliente_seleccionado = cliente


        txt_nombre.value = cliente.nombre
        txt_app.value = cliente.app
        txt_apm.value = cliente.apm
        txt_telefono.value = cliente.telefono
        txt_correo.value = cliente.correo
        txt_calle.value = cliente.calle
        txt_numero_exterior.value = cliente.numero_exterior
        txt_colonia.value = cliente.colonia


        dialogo.title = ft.Text(
            "Editar Cliente"
        )


        dialogo.actions = [

            ft.ElevatedButton(
                "Actualizar",
                icon=ft.Icons.SAVE,
                on_click=actualizar_cliente
            ),

            ft.TextButton(
                "Cancelar",
                on_click=lambda e: cerrar_dialogo()
            )

        ]


        dialogo.open = True

        page.update()



    # ACTUALIZAR CLIENTE

    def actualizar_cliente(e):

        try:

            cliente_actualizado = Cliente(

                cliente_seleccionado.id_cliente,

                txt_nombre.value,

                txt_app.value,

                txt_apm.value,

                txt_telefono.value,

                txt_correo.value,

                txt_calle.value,

                txt_numero_exterior.value,

                txt_colonia.value

            )


            cliente_dao.actualizar(
                cliente_actualizado
            )


            cerrar_dialogo()

            limpiar_campos()

            cargar_clientes()


            mostrar_mensaje(
                "Cliente actualizado correctamente."
            )


        except Exception as error:

            mostrar_mensaje(
                f"Error al actualizar cliente: {error}"
            )

    # ELIMINAR CLIENTE

    def eliminar_cliente(cliente):

        try:

            cliente_dao.eliminar(
                cliente.id_cliente
            )


            cargar_clientes()


            mostrar_mensaje(
                "Cliente eliminado correctamente."
            )


        except Exception as error:

            mostrar_mensaje(
                f"Error al eliminar cliente: {error}"
            )



    # BUSCAR CLIENTES

    def buscar_clientes(e):

        texto = txt_buscar.value.lower()

        tabla_clientes.rows.clear()


        for cliente in cliente_dao.obtener_todos():

            nombre_completo = (
                f"{cliente.nombre} {cliente.app} {cliente.apm}"
            ).lower()


            if texto in nombre_completo:

                tabla_clientes.rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(
                                ft.Text(str(cliente.id_cliente))
                            ),

                            ft.DataCell(
                                ft.Text(
                                    f"{cliente.nombre} {cliente.app} {cliente.apm}"
                                )
                            ),

                            ft.DataCell(
                                ft.Text(cliente.telefono)
                            ),

                            ft.DataCell(
                                ft.Text(cliente.correo)
                            ),

                            ft.DataCell(
                                ft.Text("Acciones")
                            )

                        ]

                    )

                )


        page.update()


    # DIALOGO

    dialogo = ft.AlertDialog(

        modal=True,

        title=ft.Text(
            "Nuevo Cliente"
        ),

        content=ft.Column(

            [

                txt_nombre,
                txt_app,
                txt_apm,
                txt_telefono,
                txt_correo,
                txt_calle,
                txt_numero_exterior,
                txt_colonia

            ],

            tight=True

        )

    )



    def nuevo_cliente(e):

        limpiar_campos()


        dialogo.title = ft.Text(
            "Nuevo Cliente"
        )


        dialogo.actions = [

            ft.TextButton(
                "Cancelar",
                on_click=lambda e: cerrar_dialogo()
            ),

            ft.ElevatedButton(
                "Guardar",
                icon=ft.Icons.SAVE,
                on_click=guardar_cliente
            )

        ]


        page.dialog = dialogo

        dialogo.open = True

        page.update()



    def cerrar_dialogo():

        dialogo.open = False

        page.update()



    def mostrar_mensaje(texto):

        page.snack_bar = ft.SnackBar(
            ft.Text(texto)
        )

        page.snack_bar.open = True

        page.update()



    txt_buscar.on_change = buscar_clientes


    cargar_clientes()



    # INTERFAZ FINAL


    return ft.Container(

        expand=True,

        padding=20,

        content=ft.Column(

            [

                ft.Row(

                    [

                        ft.Text(
                            "Gestión de Clientes",
                            size=28,
                            weight=ft.FontWeight.BOLD
                        ),


                        ft.Container(
                            expand=True
                        ),


                        ft.ElevatedButton(

                            "Nuevo Cliente",

                            icon=ft.Icons.ADD,

                            on_click=nuevo_cliente

                        )

                    ]

                ),


                txt_buscar,


                ft.Container(

                    expand=True,

                    content=tabla_clientes

                )

            ],

            expand=True

        )

    )




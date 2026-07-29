import flet as ft

from dao.contrato_dao import ContratoDAO
from modelos.contrato import Contrato


def contratos(page: ft.Page):

    contrato_dao = ContratoDAO()

    contrato_seleccionado = None


    # CAMPOS DEL FORMULARIO

    txt_fecha_firma = ft.TextField(

        label="Fecha de firma",

        width=250

    )


    txt_costo = ft.TextField(

        label="Costo",

        width=250

    )


    txt_paquetes = ft.TextField(

        label="Paquetes",

        width=250

    )


    txt_buscar = ft.TextField(

        label="Buscar contrato",

        prefix_icon=ft.Icons.SEARCH,

        expand=True

    )



    # TABLA CONTRATOS

    tabla_contratos = ft.DataTable(

        columns=[

            ft.DataColumn(
                ft.Text("ID")
            ),


            ft.DataColumn(
                ft.Text("Fecha Firma")
            ),


            ft.DataColumn(
                ft.Text("Costo")
            ),


            ft.DataColumn(
                ft.Text("Paquetes")
            ),


            ft.DataColumn(
                ft.Text("Acciones")
            )

        ],

        rows=[]

    ) 

    # DIALOGO CONTRATO

    dialogo = ft.AlertDialog(

        modal=True,

        title=ft.Text(
            "Nuevo Contrato"
        ),

        content=ft.Column(

            [

                txt_fecha_firma,

                txt_costo,

                txt_paquetes

            ],

            tight=True

        )

    )



    # CARGAR CONTRATOS

    def cargar_contratos():

        tabla_contratos.rows.clear()

        try:

            lista_contratos = contrato_dao.obtener_todo()


            for contrato in lista_contratos:

                tabla_contratos.rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(

                                ft.Text(
                                    str(contrato.id_contrato)
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    str(contrato.fecha_firma)
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    str(contrato.costo)
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    contrato.paquetes
                                )

                            ),


                            ft.DataCell(

                                ft.Row(

                                    [

                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            tooltip="Editar",

                                            on_click=lambda e, c=contrato:
                                                editar_contrato(c)

                                        ),


                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            tooltip="Eliminar",

                                            icon_color=ft.Colors.RED,

                                            on_click=lambda e, c=contrato:
                                                eliminar_contrato(c)

                                        )

                                    ]

                                )

                            )

                        ]

                    )

                )


            page.update()


        except Exception as error:

            mostrar_mensaje(

                f"Error al cargar contratos: {error}"

            )



    # LIMPIAR CAMPOS

    def limpiar_campos():

        txt_fecha_firma.value = ""

        txt_costo.value = ""

        txt_paquetes.value = "" 

    # GUARDAR CONTRATOS
    def guardar_contrato(e):

        try:

            nuevo_id = contrato_dao.obtener_ultimo_id() + 1


            contrato = Contrato(

                nuevo_id,

                txt_fecha_firma.value,

                txt_costo.value,

                txt_paquetes.value

            )


            contrato_dao.insertar(

                contrato

            )


            cerrar_dialogo()

            limpiar_campos()

            cargar_contratos()


            mostrar_mensaje(

                "Contrato registrado correctamente."

            )


        except Exception as error:

            mostrar_mensaje(

                f"Error al guardar contrato: {error}"

            )



    # EDITAR CONTRATO

    def editar_contrato(contrato):

        nonlocal contrato_seleccionado


        contrato_seleccionado = contrato


        txt_fecha_firma.value = contrato.fecha_firma

        txt_costo.value = str(contrato.costo)

        txt_paquetes.value = contrato.paquetes


        dialogo.title = ft.Text(

            "Editar Contrato"

        )


        dialogo.actions = [

            ft.ElevatedButton(

                "Actualizar",

                icon=ft.Icons.SAVE,

                on_click=actualizar_contrato

            ),


            ft.TextButton(

                "Cancelar",

                on_click=lambda e: cerrar_dialogo()

            )

        ]


        dialogo.open = True

        page.update()



    # ACTUALIZAR CONTRATO

    def actualizar_contrato(e):

        try:

            contrato_actualizado = Contrato(

                contrato_seleccionado.id_contrato,

                txt_fecha_firma.value,

                txt_costo.value,

                txt_paquetes.value

            )


            contrato_dao.actualizar(

                contrato_actualizado

            )


            cerrar_dialogo()

            limpiar_campos()

            cargar_contratos()


            mostrar_mensaje(

                "Contrato actualizado correctamente."

            )


        except Exception as error:

            mostrar_mensaje(

                f"Error al actualizar contrato: {error}"

            ) 

    # ELIMINAR CONTRATOS

    def eliminar_contrato(contrato):

        try:

            contrato_dao.eliminar(

                contrato.id_contrato

            )


            cargar_contratos()


            mostrar_mensaje(

                "Contrato eliminado correctamente."

            )


        except Exception as error:

            mostrar_mensaje(

                f"Error al eliminar contrato: {error}"

            )



    # BUSCAR CONTRATOS

    def buscar_contratos(e):

        texto = txt_buscar.value.lower()


        tabla_contratos.rows.clear()


        for contrato in contrato_dao.obtener_todo():


            if texto in str(contrato.id_contrato).lower() or texto in str(contrato.paquetes).lower():


                tabla_contratos.rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(

                                ft.Text(
                                    str(contrato.id_contrato)
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    str(contrato.fecha_firma)
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    str(contrato.costo)
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    contrato.paquetes
                                )

                            ),


                            ft.DataCell(

                                ft.Row(

                                    [

                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            tooltip="Editar",

                                            on_click=lambda e, c=contrato:
                                                editar_contrato(c)

                                        ),


                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            tooltip="Eliminar",

                                            icon_color=ft.Colors.RED,

                                            on_click=lambda e, c=contrato:
                                                eliminar_contrato(c)

                                        )

                                    ]

                                )

                            )

                        ]

                    )

                )


        page.update()



    # NUEVO CONTRATOS

    def nuevo_contrato(e):

        limpiar_campos()


        dialogo.title = ft.Text(

            "Nuevo Contrato"

        )


        dialogo.actions = [

            ft.TextButton(

                "Cancelar",

                on_click=lambda e: cerrar_dialogo()

            ),


            ft.ElevatedButton(

                "Guardar",

                icon=ft.Icons.SAVE,

                on_click=guardar_contrato

            )

        ]


        page.dialog = dialogo


        dialogo.open = True


        page.update()




    # CERRAR DIALOGOS

    def cerrar_dialogo():

        dialogo.open = False

        page.update()



    # MENSAJES

    def mostrar_mensaje(texto):

        page.snack_bar = ft.SnackBar(

            ft.Text(texto)

        )

        page.snack_bar.open = True

        page.update()



    txt_buscar.on_change = buscar_contratos


    cargar_contratos()



    # INTERFAZ FINAL

    return ft.Container(

        expand=True,

        padding=20,

        content=ft.Column(

            [

                ft.Row(

                    [

                        ft.Text(

                            "Gestión de Contratos",

                            size=28,

                            weight=ft.FontWeight.BOLD

                        ),


                        ft.Container(

                            expand=True

                        ),


                        ft.ElevatedButton(

                            "Nuevo Contrato",

                            icon=ft.Icons.ADD,

                            on_click=nuevo_contrato

                        )

                    ]

                ),


                txt_buscar,


                ft.Container(

                    expand=True,

                    content=tabla_contratos

                )

            ],

            expand=True

        )

    )
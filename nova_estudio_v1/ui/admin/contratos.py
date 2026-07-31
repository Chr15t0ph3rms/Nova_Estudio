import flet as ft

from dao.contrato_dao import ContratoDAO
from modelos.contrato import Contrato



def contratos(page: ft.Page):

    dao = ContratoDAO()

    contrato_actual = None



    # ==========================
    # CAMPOS DEL FORMULARIO
    # ==========================

    fecha_firma = ft.TextField(

        label="Fecha de Firma",

        width=250

    )


    costo = ft.TextField(

        label="Costo",

        width=250

    )


    paquetes = ft.TextField(

        label="Paquete",

        width=250

    )



    formulario = ft.Container(

        visible=False,

        bgcolor=ft.Colors.GREY_900,

        padding=20,

        border_radius=15

    )



    # ==========================
    # TABLA CONTRATOS
    # ==========================

    tabla = ft.DataTable(

        expand=True,

        column_spacing=45,

        horizontal_margin=30,


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




    # ==========================
    # LIMPIAR
    # ==========================

    def limpiar():

        fecha_firma.value = ""

        costo.value = ""

        paquetes.value = ""




    # ==========================
    # CARGAR TABLA
    # ==========================

    def cargar():

        tabla.rows.clear()


        contratos_lista = dao.obtener_todo()



        for contrato in contratos_lista:


            tabla.rows.append(

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

                            ft.Container(

                                width=130,


                                content=ft.Row(

                                    [


                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            icon_color=ft.Colors.BLUE_400,

                                            tooltip="Editar contrato",

                                            on_click=lambda e, c=contrato: editar(c)

                                        ),



                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            icon_color=ft.Colors.RED_400,

                                            tooltip="Eliminar contrato",

                                            on_click=lambda e, c=contrato: eliminar(c)

                                        )


                                    ],

                                    spacing=8

                                )

                            )

                        )


                    ]

                )

            )


        page.update() 

    # ==========================
    # MOSTRAR FORMULARIO
    # ==========================

    def mostrar_formulario(titulo):

        formulario.content = ft.Column(

            [

                ft.Text(

                    titulo,

                    size=25,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.WHITE

                ),



                ft.Row(

                    [

                        fecha_firma,

                        costo

                    ]

                ),



                ft.Row(

                    [

                        paquetes

                    ]

                ),



                ft.Row(

                    [

                        ft.ElevatedButton(

                            "Guardar",

                            icon=ft.Icons.SAVE,

                            on_click=guardar

                        ),



                        ft.TextButton(

                            "Cancelar",

                            on_click=cerrar_formulario

                        )

                    ]

                )


            ]

        )


        formulario.visible = True

        page.update()




    # ==========================
    # CERRAR FORMULARIO
    # ==========================

    def cerrar_formulario(e=None):

        formulario.visible = False

        limpiar()

        page.update()




    # ==========================
    # NUEVO CONTRATO
    # ==========================

    def nuevo_contrato(e):

        nonlocal contrato_actual


        contrato_actual = None


        limpiar()


        mostrar_formulario(

            "Nuevo Contrato"

        )




    # ==========================
    # GUARDAR CONTRATO
    # ==========================

    def guardar(e):

        try:


            nuevo = Contrato(

                id_contrato=dao.obtener_ultimo_id()+1,


                fecha_firma=fecha_firma.value,


                costo=float(

                    costo.value

                    if costo.value

                    else 0

                ),


                paquetes=paquetes.value

            )



            dao.insertar(nuevo)



            cerrar_formulario()


            cargar()



            mostrar_mensaje(

                "Contrato agregado correctamente"

            )



        except Exception as error:


            mostrar_mensaje(

                f"Error: {error}"

            )





    # ==========================
    # EDITAR CONTRATO
    # ==========================

    def editar(contrato):

        nonlocal contrato_actual


        contrato_actual = contrato



        fecha_firma.value = str(

            contrato.fecha_firma

        )


        costo.value = str(

            contrato.costo

        )


        paquetes.value = contrato.paquetes



        mostrar_formulario(

            "Editar Contrato"

        )



        formulario.content.controls[-1].controls[0].text = "Actualizar"


        formulario.content.controls[-1].controls[0].on_click = actualizar



        page.update()




    # ==========================
    # ACTUALIZAR CONTRATO
    # ==========================

    def actualizar(e):

        try:


            contrato_actual.fecha_firma = fecha_firma.value


            contrato_actual.costo = float(

                costo.value

                if costo.value

                else 0

            )


            contrato_actual.paquetes = paquetes.value



            dao.actualizar(

                contrato_actual

            )



            cerrar_formulario()


            cargar()



            mostrar_mensaje(

                "Contrato actualizado correctamente"

            )



        except Exception as error:


            mostrar_mensaje(

                f"Error al actualizar: {error}"

            )




    # ==========================
    # MENSAJES
    # ==========================

    def mostrar_mensaje(texto):

        page.snack_bar = ft.SnackBar(

            ft.Text(texto)

        )


        page.snack_bar.open = True


        page.update() 

    # ==========================
    # ELIMINAR CONTRATO
    # ==========================

    def eliminar(contrato):


        def aceptar(e):

            dao.eliminar(

                contrato.id_contrato

            )


            dialogo_eliminar.open = False

            page.update()


            cargar()


            mostrar_mensaje(

                "Contrato eliminado correctamente"

            )



        def cancelar(e):

            dialogo_eliminar.open = False

            page.update()



        dialogo_eliminar = ft.AlertDialog(

            modal=True,


            title=ft.Text(

                "Eliminar contrato"

            ),


            content=ft.Text(

                "¿Seguro que deseas eliminar este contrato?"

            ),


            actions=[


                ft.TextButton(

                    "Cancelar",

                    on_click=cancelar

                ),


                ft.ElevatedButton(

                    "Aceptar",

                    icon=ft.Icons.DELETE,

                    on_click=aceptar

                )

            ]

        )


        page.dialog = dialogo_eliminar

        dialogo_eliminar.open = True

        page.update()





    # ==========================
    # BOTÓN NUEVO CONTRATO
    # ==========================

    boton_nuevo = ft.ElevatedButton(

        "Nuevo Contrato",

        icon=ft.Icons.ADD,

        on_click=nuevo_contrato

    )




    # ==========================
    # CARGAR DATOS INICIALES
    # ==========================

    cargar()




    # ==========================
    # INTERFAZ FINAL
    # ==========================

    return ft.Container(

        expand=True,

        padding=20,


        content=ft.Column(

            [

                ft.Row(

                    [

                        ft.Text(

                            "Gestión de Contratos",

                            size=30,

                            weight=ft.FontWeight.BOLD,

                            color=ft.Colors.WHITE

                        ),



                        ft.Container(

                            expand=True

                        ),



                        boton_nuevo

                    ]

                ),



                ft.Divider(),



                formulario,



                ft.Container(

                    height=0

                ),



                ft.Container(

                    padding=0,

                    content=ft.Column(

                        [

                            tabla

                        ],

                        spacing=0

                    )

                )

            ],


            expand=True,

            spacing=0

        )

    )
import flet as ft

from dao.cliente_dao import ClienteDAO
from modelos.cliente import Cliente


def clientes(page: ft.Page):

    dao = ClienteDAO()

    cliente_actual = None


    # ==========================
    # CAMPOS DEL FORMULARIO
    # ==========================

    nombre = ft.TextField(
        label="Nombre",
        width=250
    )

    app = ft.TextField(
        label="Apellido Paterno",
        width=250
    )

    apm = ft.TextField(
        label="Apellido Materno",
        width=250
    )

    telefono = ft.TextField(
        label="Teléfono",
        width=250
    )

    correo = ft.TextField(
        label="Correo",
        width=250
    )

    calle = ft.TextField(
        label="Calle",
        width=250
    )

    numero_exterior = ft.TextField(
        label="Número Exterior",
        width=250
    )

    colonia = ft.TextField(
        label="Colonia",
        width=250
    )


    formulario = ft.Container(

        visible=False,

        bgcolor=ft.Colors.GREY_900,

        padding=20,

        border_radius=15

    )



    # ==========================
    # TABLA MEJORADA
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
                ft.Text("Nombre")
            ),

            ft.DataColumn(
                ft.Text("Apellido P.")
            ),

            ft.DataColumn(
                ft.Text("Apellido M.")
            ),

            ft.DataColumn(
                ft.Text("Teléfono")
            ),

            ft.DataColumn(
                ft.Text("Correo")
            ),

            ft.DataColumn(
                ft.Text("Calle")
            ),

            ft.DataColumn(
                ft.Text("Número")
            ),

            ft.DataColumn(
                ft.Text("Colonia")
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

        nombre.value = ""

        app.value = ""

        apm.value = ""

        telefono.value = ""

        correo.value = ""

        calle.value = ""

        numero_exterior.value = ""

        colonia.value = ""



    # ==========================
    # CARGAR TABLA
    # ==========================

    def cargar():

        tabla.rows.clear()


        clientes_lista = dao.obtener_todos()


        for cliente in clientes_lista:


            tabla.rows.append(

                ft.DataRow(

                    cells=[

                        ft.DataCell(
                            ft.Text(
                                str(cliente.id_cliente)
                            )
                        ),


                        ft.DataCell(
                            ft.Text(
                                cliente.nombre
                            )
                        ),


                        ft.DataCell(
                            ft.Text(
                                cliente.app
                            )
                        ),


                        ft.DataCell(
                            ft.Text(
                                cliente.apm
                            )
                        ),


                        ft.DataCell(
                            ft.Text(
                                cliente.telefono
                            )
                        ),


                        ft.DataCell(
                            ft.Text(
                                cliente.correo
                            )
                        ),


                        ft.DataCell(
                            ft.Text(
                                cliente.calle
                            )
                        ),


                        ft.DataCell(
                            ft.Text(
                                str(cliente.numero_exterior)
                            )
                        ),


                        ft.DataCell(
                            ft.Text(
                                cliente.colonia
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

                                            tooltip="Editar cliente",

                                            on_click=lambda e,c=cliente:
                                            editar(c)

                                        ),


                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            icon_color=ft.Colors.RED_400,

                                            tooltip="Eliminar cliente",

                                            on_click=lambda e,c=cliente:
                                            eliminar(c)

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

                        nombre,

                        app

                    ]

                ),


                ft.Row(

                    [

                        apm,

                        telefono

                    ]

                ),


                ft.Row(

                    [

                        correo,

                        calle

                    ]

                ),


                ft.Row(

                    [

                        numero_exterior,

                        colonia

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
    # NUEVO CLIENTE
    # ==========================

    def nuevo_cliente(e):

        nonlocal cliente_actual

        cliente_actual = None


        limpiar()


        mostrar_formulario(

            "Nuevo Cliente"

        )




    # ==========================
    # GUARDAR CLIENTE
    # ==========================

    def guardar(e):

        try:

            numero = 0


            if numero_exterior.value:

                numero = int(
                    numero_exterior.value
                )



            nuevo = Cliente(

                id_cliente=dao.obtener_ultimo_id()+1,

                nombre=nombre.value,

                app=app.value,

                apm=apm.value,

                telefono=telefono.value,

                correo=correo.value,

                calle=calle.value,

                numero_exterior=numero,

                colonia=colonia.value

            )



            dao.insertar(nuevo)



            cerrar_formulario()

            cargar()



            mostrar_mensaje(

                "Cliente agregado correctamente"

            )



        except Exception as error:


            mostrar_mensaje(

                f"Error: {error}"

            )





    # ==========================
    # EDITAR CLIENTE
    # ==========================

    def editar(cliente):

        nonlocal cliente_actual


        cliente_actual = cliente



        nombre.value = cliente.nombre

        app.value = cliente.app

        apm.value = cliente.apm

        telefono.value = cliente.telefono

        correo.value = cliente.correo

        calle.value = cliente.calle

        numero_exterior.value = str(
            cliente.numero_exterior
        )

        colonia.value = cliente.colonia



        mostrar_formulario(

            "Editar Cliente"

        )


        formulario.content.controls[-1].controls[0].text = "Actualizar"

        formulario.content.controls[-1].controls[0].on_click = actualizar


        page.update()




    # ==========================
    # ACTUALIZAR CLIENTE
    # ==========================

    def actualizar(e):

        try:


            cliente_actual.nombre = nombre.value

            cliente_actual.app = app.value

            cliente_actual.apm = apm.value

            cliente_actual.telefono = telefono.value

            cliente_actual.correo = correo.value

            cliente_actual.calle = calle.value


            cliente_actual.numero_exterior = int(

                numero_exterior.value

                if numero_exterior.value

                else 0

            )


            cliente_actual.colonia = colonia.value



            dao.actualizar(

                cliente_actual

            )



            cerrar_formulario()

            cargar()



            mostrar_mensaje(

                "Cliente actualizado correctamente"

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
    # ELIMINAR CLIENTE
    # ==========================

    def eliminar(cliente):


        def aceptar(e):

            dao.eliminar(

                cliente.id_cliente

            )


            dialogo_eliminar.open = False

            page.update()


            cargar()


            mostrar_mensaje(

                "Cliente eliminado correctamente"

            )



        def cancelar(e):

            dialogo_eliminar.open = False

            page.update()



        dialogo_eliminar = ft.AlertDialog(

            modal=True,


            title=ft.Text(

                "Eliminar cliente"

            ),


            content=ft.Text(

                "¿Seguro que deseas eliminar este cliente?"

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
    # BOTÓN NUEVO CLIENTE
    # ==========================

    boton_nuevo = ft.ElevatedButton(

        "Nuevo Cliente",

        icon=ft.Icons.ADD,

        on_click=nuevo_cliente

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
                        "Gestión de Clientes",
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


            # AQUÍ VA LA TABLA
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
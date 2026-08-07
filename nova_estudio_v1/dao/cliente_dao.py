from database.conexion import Conexion
from modelos.cliente import Cliente

class ClienteDAO:

    # OBTENER DATOS EXTRA DEL CLIENTE (dirección, teléfono) A PARTIR
    # DE SU id_usuario (ya logueado vía la tabla usuario)

    @staticmethod
    def obtener_por_usuario(id_usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT id_cliente, telefono, calle, numero_exterior, colonia FROM cliente WHERE id_usuario = %s",
            (id_usuario,)
        )

        registro = cursor.fetchone()

        cursor.close()
        conexion.close()

        return registro  # None si este usuario no tiene fila en cliente todavía

    # Login de cliente delegado a UsuarioDAO.login()
    @staticmethod
    def login(correo, contraseña):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT id_cliente, nombre, correo FROM cliente WHERE correo = %s AND contraseña = %s",
            (correo, contraseña)
        )

        registro = cursor.fetchone()

        cursor.close()
        conexion.close()

        return registro  # None si no hay coincidencia, o (id_cliente, nombre, correo)

    # OBTENER TODOS LOS CLIENTES

    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM cliente")
        registros = cursor.fetchall()

        clientes = []

        for registro in registros:
            cliente = Cliente(
                id_cliente=registro[0],
                nombre=registro[1],
                app=registro[2],
                apm=registro[3],
                telefono=registro[4],
                correo=registro[5],
                calle=registro[6],
                numero_exterior=registro[7],
                colonia=registro[8]
            )
            clientes.append(cliente)

        cursor.close()
        conexion.close()

        return clientes

    # INSERTAR CLIENTE

    def insertar(self, cliente):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO cliente
        (id_cliente, nombre, app, apm, telefono, correo, calle, numero_exterior, colonia)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            cliente.id_cliente,
            cliente.nombre,
            cliente.app,
            cliente.apm,
            cliente.telefono,
            cliente.correo,
            cliente.calle,
            cliente.numero_exterior,
            cliente.colonia
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # ACTUALIZAR CLIENTE

    def actualizar(self, cliente):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE cliente
        SET
            nombre=%s,
            app=%s,
            apm=%s,
            telefono=%s,
            correo=%s,
            calle=%s,
            numero_exterior=%s,
            colonia=%s
        WHERE id_cliente=%s
        """

        cursor.execute(sql, (
            cliente.nombre,
            cliente.app,
            cliente.apm,
            cliente.telefono,
            cliente.correo,
            cliente.calle,
            cliente.numero_exterior,
            cliente.colonia,
            cliente.id_cliente
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # ELIMINAR CLIENTE

    def eliminar(self, id_cliente):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM cliente WHERE id_cliente = %s",
            (id_cliente,)
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    # OBTENER ÚLTIMO ID

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT MAX(id_cliente) FROM cliente")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:
            return 0

        return resultado[0]

    # Método alias para compatibilidad con llamadas que usan el nombre singular
    def obtener_todo(self):
        return self.obtener_todos()

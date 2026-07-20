from database.conexion import Conexion
from modelos.cliente import Cliente

class ClienteDAO:

    #SELECT * FROM cliente
    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM agencia")
        registros = cursor.fetchall()

        clientes = []
        for registro in registros : 
            cliente = Cliente(
                id_cliente = registro[0],
                nombre = registro[1],
                app = registro[2],
                apm = registro[3],
                telefono = registro[4],
                correo = registro[5],
                calle = registro[6],
                colonia = registro[7],
                numero_exterior = registro[8]
            )
            clientes.append(cliente)
        cursor.close()
        conexion.close()
        return clientes

    # INSERT
    def insertar(self, cliente):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO cliente(id_cliente, nombre, app, apm, telefono, correo, calle, colonia, numero_exterior)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            cliente.id_cliente,
            cliente.nombre,
            cliente.app,
            cliente.apm,
            cliente.telefono,
            cliente.correo,
            cliente.calle,
            cliente.colonia,
            cliente.numero_exterior
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # UPDATE
    def actualizar(self, cliente):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE cliente
        SET nombre = %s, app = %s, apm = %s, telefono = %s, correo = %s, calle = %s, colonia = %s, numero_exterior = %s
        WHERE id_cliente = %s
        """

        cursor.execute(sql, (
            cliente.nombre,
            cliente.app,
            cliente.apm,
            cliente.telefono,
            cliente.correo,
            cliente.calle,
            cliente.colonia,
            cliente.numero_exterior,
            cliente.id_cliente
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # DELETE
    def eliminar(self,id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM cliente WHERE id_cliente = %s",(id,))

        conexion.commit()
        cursor.close()
        conexion.close()


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
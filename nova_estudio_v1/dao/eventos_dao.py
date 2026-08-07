from database.conexion import Conexion
from modelos.eventos import Eventos

class EventosDAO:

    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM evento")
        registros = cursor.fetchall()

        eventos = []
        for registro in registros :
            evento = Eventos(
                id_evento = registro[0],
                nombre = registro[1],
                fecha = registro[2],
                hora = registro[3],
                calle = registro[4],
                colonia = registro[5],
                numero_exterior = registro[6],
                costo = registro[7],
                id_cliente = registro[8] if len(registro) > 8 else None,
                estado = registro[9] if len(registro) > 9 and registro[9] else "En proceso"
            )
            eventos.append(evento)
        cursor.close()
        conexion.close()
        return eventos

    # SELECT solo los eventos de un cliente en específico
    def obtener_por_cliente(self, id_cliente):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM evento WHERE id_cliente = %s ORDER BY id_evento DESC", (id_cliente,))
        registros = cursor.fetchall()

        eventos = []
        for registro in registros:
            evento = Eventos(
                id_evento = registro[0],
                nombre = registro[1],
                fecha = registro[2],
                hora = registro[3],
                calle = registro[4],
                colonia = registro[5],
                numero_exterior = registro[6],
                costo = registro[7],
                id_cliente = registro[8] if len(registro) > 8 else None,
                estado = registro[9] if len(registro) > 9 and registro[9] else "En proceso"
            )
            eventos.append(evento)

        cursor.close()
        conexion.close()
        return eventos

    def insertar(self, evento):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO evento(id_evento, nombre, fecha, hora, calle, colonia, numero_exterior, costo, id_cliente, estado)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            evento.id_evento,
            evento.nombre,
            evento.fecha,
            evento.hora,
            evento.calle,
            evento.colonia,
            evento.numero_exterior,
            evento.costo,
            evento.id_cliente,
            evento.estado
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, evento):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE evento
        SET nombre = %s, fecha = %s, hora = %s, calle = %s, colonia = %s, numero_exterior = %s, costo = %s, estado = %s
        WHERE id_evento = %s
        """

        cursor.execute(sql, (
                        evento.nombre,
                        evento.fecha,
                        evento.hora,
                        evento.calle,
                        evento.colonia,
                        evento.numero_exterior,
                        evento.costo,
                        evento.estado,
                        evento.id_evento
                        ) )

        conexion.commit()
        cursor.close()
        conexion.close()

    # Cambiar solo el estado (para "Cancelar evento", por ejemplo)
    def actualizar_estado(self, id_evento, nuevo_estado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "UPDATE evento SET estado = %s WHERE id_evento = %s",
            (nuevo_estado, id_evento)
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self,id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM evento WHERE id_evento = %s",(id,))

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT MAX(id_evento) FROM evento")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:
            return 0
        return resultado[0]

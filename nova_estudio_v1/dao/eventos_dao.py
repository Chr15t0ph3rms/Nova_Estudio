from database.conexion import Conexion
from modelos.eventos import Eventos

class EventosDAO:

    #SELECT * FROM eventos
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
                sonido = registro[8]
            )
            eventos.append(evento)
        cursor.close()
        conexion.close()
        return eventos

    # INSERT
    def insertar(self, evento):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO evento(id_evento, nombre, fecha, hora, calle, colonia, numero_exterior, costo, sonido)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
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
            evento.sonido
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # UPDATE
    def actualizar(self, evento):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE evento
        SET nombre = %s, fecha = %s, hora = %s, calle = %s, colonia = %s, numero_exterior = %s, costo = %s, sonido = %s
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
                        evento.sonido,
                        evento.id_evento
                        ) )
        
        conexion.commit()
        cursor.close()
        conexion.close()

    # DELETE
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



from database.conexion import Conexion
from modelos.inventario import Inventario

class InventarioDAO:

    #SELECT * FROM libro
    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM inventario")
        registros = cursor.fetchall()

        inventarios = []
        for registro in registros : 
            inventario = Inventario(
                id_inventario = registro[0],
                nombre = registro[1],
                tipo = registro[2],
                estado = registro[3],
                cantidad = registro[4],
                disponible = registro[5]
            )
            inventarios.append(inventario)
        cursor.close()
        conexion.close()
        return inventarios

    # INSERT
    def insertar(self, inventario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO inventario(id_inventario, nombre, tipo, estado, cantidad, disponible)
        VALUES(%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            inventario.id_inventario,
            inventario.nombre,
            inventario.tipo,
            inventario.estado,
            inventario.cantidad,
            inventario.disponible
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # UPDATE
    def actualizar(self, inventario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE inventario
        SET nombre = %s, tipo = %s, estado = %s, cantidad = %s, disponible = %s
        WHERE id_inventario = %s
        """

        cursor.execute(sql, (
                       inventario.nombre,
                       inventario.tipo,
                       inventario.estado,
                       inventario.cantidad,
                       inventario.disponible,
                       inventario.id_inventario
                       ) )
        
        conexion.commit()
        cursor.close()
        conexion.close()

    # DELETE
    def eliminar(self,id):
       conexion = Conexion.obtener_conexion()
       cursor = conexion.cursor()

       cursor.execute("DELETE FROM inventario WHERE id_inventario = %s",(id,))

       conexion.commit()
       cursor.close()
       conexion.close()


    def obtener_ultimo_id(self):
       conexion = Conexion.obtener_conexion()
       cursor = conexion.cursor()

       cursor.execute("SELECT MAX(id_inventario) FROM inventario")
       resultado = cursor.fetchone()

       cursor.close()
       conexion.close()

       if resultado[0] is None:
           return 0
       return resultado[0] 



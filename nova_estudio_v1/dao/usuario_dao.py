from database.conexion import Conexion


class UsuarioDAO:


    @staticmethod
    def login(correo, password):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()


        try:

            sql = """
            SELECT 
                id_usuario,
                nombre,
                apellido,
                correo,
                rol
            FROM usuario
            WHERE correo = %s
            AND password = %s
            """


            cursor.execute(
                sql,
                (
                    correo,
                    password
                )
            )


            usuario = cursor.fetchone()


            return usuario


        except Exception as error:

            print(
                "Error login:",
                error
            )

            return None


        finally:

            cursor.close()
            conexion.close()
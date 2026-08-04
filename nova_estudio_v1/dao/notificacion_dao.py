from database.conexion import Conexion


class NotificacionDAO:
    @staticmethod
    def obtener_notificaciones():
        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        notificaciones = []

        try:
            # Nuevos clientes

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM cliente
                """
            )

            clientes = cursor.fetchone()[0]

            if clientes > 0:
                notificaciones.append(
                    f"{clientes} cliente(s) registrado(s)"
                )

            # Eventos registrados

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM evento
                """
            )

            eventos = cursor.fetchone()[0]

            if eventos > 0:
                notificaciones.append(
                    f"{eventos} evento(s) creado(s)"
                )

            # Pagos

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM pago
                """
            )

            pagos = cursor.fetchone()[0]

            if pagos > 0:
                notificaciones.append(
                    f"{pagos} pago(s) registrado(s)"
                )

            # Contratos

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM contrato
                """
            )

            contratos = cursor.fetchone()[0]

            if contratos > 0:
                notificaciones.append(
                    f"{contratos} contrato(s) generado(s)"
                )

            return notificaciones

        except Exception as error:
            print(
                "Error notificaciones:",
                error
            )

            return []

        finally:
            cursor.close()

            conexion.close()

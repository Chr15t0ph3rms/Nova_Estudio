from database.conexion import Conexion


class DashboardDAO:


    @staticmethod
    def contar(tabla):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        try:

            cursor.execute(
                f"SELECT COUNT(*) FROM {tabla}"
            )

            resultado = cursor.fetchone()[0]

            return resultado


        except Exception as error:

            print("Error contando:", tabla, error)

            return 0


        finally:

            cursor.close()
            conexion.close()



    # ==============================
    # SUMA DE INGRESOS
    # ==============================

    @staticmethod
    def obtener_ingresos():

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        try:

            cursor.execute(
                """
                SELECT COALESCE(SUM(monto),0)
                FROM pago
                """
            )

            resultado = cursor.fetchone()[0]

            return float(resultado)


        except Exception as error:

            print("Error ingresos:", error)

            return 0


        finally:

            cursor.close()
            conexion.close()



    # ==============================
    # ESTADISTICAS GENERALES
    # ==============================

    @staticmethod
    def obtener_estadisticas():


        return {


            "clientes":
            DashboardDAO.contar("cliente"),


            "eventos":
            DashboardDAO.contar("evento"),


            "empleados":
            DashboardDAO.contar("empleados"),


            "inventario":
            DashboardDAO.contar("inventario"),


            "djs":
            DashboardDAO.contar("dj"),


            "contratos":
            DashboardDAO.contar("contrato"),


            "pagos":
            DashboardDAO.contar("pago"),


            "ingresos":
            DashboardDAO.obtener_ingresos()

        }
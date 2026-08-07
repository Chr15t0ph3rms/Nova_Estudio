class Pago:

    def __init__(
        self,
        id_pago,
        id_contrato,
        fecha_pago,
        monto,
        estado,
        id_cliente=None,
        id_evento=None
    ):

        self.id_pago = id_pago
        self.id_contrato = id_contrato
        self.fecha_pago = fecha_pago
        self.monto = monto
        self.estado = estado
        self.id_cliente = id_cliente
        self.id_evento = id_evento

    def mostrar_info(self):

        return (
            f"ID Pago: {self.id_pago}, "
            f"ID Contrato: {self.id_contrato}, "
            f"Fecha: {self.fecha_pago}, "
            f"Monto: {self.monto}, "
            f"Estado: {self.estado}"
        )

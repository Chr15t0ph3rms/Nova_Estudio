class Contrato:
    
    #Constructor
    def __init__(self, id_contrato, fecha_firma, costo, paquetes):
        self.id_contrato = id_contrato
        self.fecha_firma = fecha_firma
        self.costo = costo
        self.paquetes = paquetes

    def mostrar_info(self):
        return f"ID: {self.id_contrato}, Fecha: {self.fecha_firma}, Costo: {self.costo}, Paquetes: {self.paquetes}"
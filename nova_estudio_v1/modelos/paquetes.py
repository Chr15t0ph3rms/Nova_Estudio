class Paquetes:
    
    #Constructor
    def __init__(self, id_paquetes, nombre, tipo_paquete, costo, descripcion):
        self.id_paquetes = id_paquetes
        self.nombre = nombre
        self.tipo_paquete = tipo_paquete
        self.costo = costo
        self.descripcion = descripcion

    def mostrar_info(self):
        return f"ID: {self.id_paquetes}, Nombre: {self.nombre}, Tipo: {self.tipo_paquete}, Costo: {self.costo}, Descripción: {self.descripcion}"
class Inventario    :
    
    #Constructor
    def __init__(self, id_inventario, nombre, tipo, estado, cantidad, disponible):
        self.id_inventario = id_inventario
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado
        self.cantidad = cantidad
        self.disponible = disponible

    def prestar(self):
        self.disponible = False
    
    def devolver(self):
        self.disponible = True

    def mostrar_info(self):
        disponible = "Disponible" if self.disponible else "No disponible"
        return f"ID: {self.id_inventario}, Nombre: {self.nombre}, Tipo: {self.tipo}, Estado: {self.estado}, Cantidad: {self.cantidad}, Disponible: {disponible}"
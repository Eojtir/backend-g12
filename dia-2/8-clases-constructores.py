class Producto:
    def __init__(self, nombre, precio, disponibilidad, imagen):
        self.nombre = nombre
        self.precio = precio
        self.disponibilidad = disponibilidad
        self.imagen =imagen

    def mostrar_imagen(self):
        return self.imagen




colonia = Producto('ferrary',55, True ,'https://google.com')

print(colonia.mostrar_imagen())
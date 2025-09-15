#Agregar elementos
class tienda:
    def __init__(self):
        self.productos=[]

    def agregar_producto(self, producto):
        self.productos.append(producto)

Tienda = tienda()
Tienda.agregar_producto("Camiseta")
Tienda.agregar_producto("Zapatos")
Tienda.agregar_producto("Saco")
Tienda.agregar_producto("Gorra")
print(Tienda.productos)



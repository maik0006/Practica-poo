#Eliminar elementos
class tienda:
    def __init__(self):
        self.productos=["Camiseta","Zapatos","Saco","Gorra"]

    def eliminar_producto(self, producto):
        self.productos.remove(producto)


Tienda = tienda()
Tienda.eliminar_producto("Camiseta")
print(Tienda.productos)


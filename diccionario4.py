class Inventario:
    #Maikoll Daniel Torres Fandiño
    def __init__(self):
        self.stock = {} 

    def agregar_producto(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def mostrar_inventario(self):
        for producto, cantidad in self.stock.items():
            print(f"{producto}: {cantidad} unidades")

inv = Inventario()
inv.agregar_producto("Teclado", 5)
inv.agregar_producto("Mouse", 3)
inv.agregar_producto("Teclado", 2)
inv.mostrar_inventario()


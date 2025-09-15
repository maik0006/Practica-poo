class tienda:
    def __init__(self):
        self.productos =["Camisa","Zapatos","Gorra"]

    def buscar_producto(self,producto):
        return producto in self.productos
    
Tienda=tienda()
print(Tienda.buscar_producto("Camisa"))
        
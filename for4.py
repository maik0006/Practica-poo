class TablaMultiplicar:
    #Maikoll Daniel Torres Fandiño
    def __init__(self, numero):
        self.numero = numero

    def mostrar_tabla(self):
        for i in range(1, 11):
            print(f"{self.numero} x {i} = {self.numero * i}")

t = TablaMultiplicar(7)
t.mostrar_tabla()

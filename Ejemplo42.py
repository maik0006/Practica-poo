class empresas:
    def __init__(self, rut, Nombre, tamaño):

        self.rut=rut
        self.Nombre=Nombre
        self.tamaño=tamaño


empresas1= empresas(5234543,"Nescafe","Macroempresa")
print("-"*30)
print(empresas1.rut, empresas1.Nombre, empresas1.tamaño)


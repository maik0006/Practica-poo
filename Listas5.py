class Numeros:
    def __init__(self):
        self.numeros = [23, 45, 67 ,76]
    def calcular_suma(self):
        return sum(self.numeros)
    
numeros= Numeros()
print("El resutado de la suma es: ", numeros.calcular_suma())
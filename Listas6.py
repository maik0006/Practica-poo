#Frase
class Frases:
    def __init__(self):
        self.palabras =[]

    def agregar_palabra(self,palabra):
        self.palabras.append(palabra)

palabras = Frases()
palabras.agregar_palabra("Hola")
palabras.agregar_palabra("Juan")
print(palabras.palabras)
  
        
class animales:
    def __init__(self,especie,familia,genero):

        self.especie=especie
        self.familia=familia
        self.genero=genero

animales1=animales("Homo Sapiens","Hominidae","homo")
print("-"*50)
print(animales1.especie, animales1.familia, animales1.genero)
animales2=animales("Canis lupus familiaris","Canidae","Canis")
print("-"*50)
print(animales2.especie, animales2.familia, animales2.genero)
print("-"*50)
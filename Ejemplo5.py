class persona:
    #Crea el objeto
    def __new__(cls,nombre,edad):
     return super().__new__(cls)
    
    #Se definen e inicializan los atributos
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    #Sirve para destruir un objeto
    def __del__(self):
        print(f"Objeto {self.nombre} destruido")
    
#LLamar los atributos
ana=persona("Ana",30)
carlos=persona("carlos",47)

print(f'{ana.nombre},{ana.edad},{carlos.nombre},{carlos.edad}')

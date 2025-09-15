class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

personas=[Persona("Juan",17),Persona("Sergio",28),Persona("Camilo",56),Persona("Mariana",76)]
for persona in personas:
    print(persona.nombre)

     


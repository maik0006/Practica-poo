class Persona:
    def __init__(self):
        self.personas=[]

personas=[Persona("Juan",17),Persona("Sergio",28),Persona("Camilo",56),Persona("Mariana",76)]
for persona in personas:
    print(persona.nombre)
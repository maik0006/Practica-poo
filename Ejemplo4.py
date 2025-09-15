class Vehiculo:
    def __init__(self, motor, llantas, capacidad):
        self.motor = motor
        self.llantas = llantas
        self.capacidad = capacidad
 
carro1= Vehiculo("2600","R14","6 pasajeros")

print(carro1.motor)
print(carro1.llantas)
print(carro1.capacidad)


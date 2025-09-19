class Usuario:
    def __init__(self, clave):
        self.clave = clave

    def login(self):
        intento = ""
        while intento != self.clave:
            intento = input("Ingrese contraseña: ")
        print("Acceso concedido")

u = Usuario("1234")
u.login()

class Menu:
    #Maikol Daniel Torres Fandiño
    def mostrar(self):
        opcion = ""
        while opcion != "3":
            print("1) Saludar\n2) Despedir\n3) Salir")
            opcion = input("Elige: ")
            if opcion == "1":
                print("Hola!")
            elif opcion == "2":
                print("Adiós!")
        print("Programa terminado")

menu = Menu()
menu.mostrar()

import os

class Menu:
    _opc = None

    def __init__(self) -> None:
        pass
    
    def menu_titulo(self):
        #os.system('cls')
        print("Presiona Enter para continuar...")
        input()
        print("<----- Veterinaria ----->")
    
    def menu_principal(self):
        print("<----- Menu Principal ----->\n")
        print("1. Iniciar sesion.")
        print("2. Registrar usuario.")
        print("0. Salir")
        self._opc = int((input("Opc -> ")))
        
    def menu_sesion_iniciada(self, nombre):
        print(f"<----- Bienvenido {nombre} ----->\n")
        print("1. Comprar productos.")
        print("2. Registar una cita.")
        print("3. Modificar perfil.")
        print("0. Cerrar sesion.")
        self._opc = int((input("Opc -> ")))
        
    def menu_modificar_perfil(self):
        print("<----- Modificar Perfil ----->\n")
        print("1. User.")
        print("2. Nombre.")
        print("3. Password.")
        print("4. Genero.")
        print("5. Telefono.")
        print("6. Email.")
        print("0. Regresar.")
        self._opc = int(input("Opc -> "))
        
    def registrar_cita(self):
        pass
        
    @property
    def opc(self):
        return self._opc
        
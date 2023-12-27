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
        print("3. Buscar usuario.")
        
        print("0. Salir")
        self._opc = int((input("Opc -> ")))
        
    def menu_sesion_iniciada(self, nombre):
        print(f"<----- Bienvenido {nombre} ----->\n")
        print("1. Comprar productos.")
        print("2. Registar una cita.")
        print("3. Ver mis mascotas.")
        print("4. Modificar perfil.")
        print("0. Cerrar sesion.")
        self._opc = int((input("Opc -> ")))
        
    def menu_acutalizar_perfil_usuario(self):
        print("<----- Modificar Perfil ----->\n")
        print("1. User.")
        print("2. Nombre.")
        print("3. Password.")
        print("4. Genero.")
        print("5. Telefono.")
        print("6. Email.")
        print("0. Regresar.")
        self._opc = int(input("Opc -> "))
        
    def menu_mascotas(self):
        print("<----- Menu Mascotas ----->\n")
        
        print("1. Ver mis mascotas.")
        print("2. Agregar una nueva mascota.")
        print("3. Actualizar perfil de una mascota.")
        print("4. Eliminar perfil de una mascota")
        print("0. Regresar.")
        self._opc = int(input("Opc -> "))

        
    def menu_actualizar_perfil_mascota(self):
        print("<----- Menu Modificar ----->\n")
        
        print("1. Nombre.")
        print("2. Fecha de nacimiento.")
        print("3. Tipo de mascota.")
        print("4. Raza.")
        print("5. Peso.")
        print("6. Genero.")
        print("7. Color.")
        print("0. Regresar")
        print("Opc -> ")
        self.opc = int(input("Opc -> "))
        
    def registrar_cita(self):
        pass
        
    @property
    def opc(self):
        return self._opc
        
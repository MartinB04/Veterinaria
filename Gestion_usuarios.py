from Menu import *
from IOFile import *
from Gestion_mascotas import *

menu = Menu()
iofile = IOFile()

class Gestion_usuarios:

    lista_usuarios = None
    usuario_actual = None
    
    def __init__(self, lista) -> None:
        self.lista_usuarios = lista
        
    def actualizar_perfil(self,):
    
        while True:
        
            menu.menu_titulo()
            menu.menu_acutalizar_perfil_usuario()
            try: opcion = int(menu.opcion_menu)
            except Exception as e: 
                print(f"Error, {e}.")
                opcion = None
        
            if opcion == 1: self.usuario_actual.usuario = input("User -> ")
            elif opcion == 2: self.usuario_actual.nombre = input("Nombre -> ")
            elif opcion == 3: self.usuario_actual.password = input("Password -> ")
            elif opcion == 4: self.usuario_actual.genero = input("Genero -> ")
            elif opcion == 5: self.usuario_actual.telefono = input("Telefono -> ")
            elif opcion == 6: self.usuario_actual.email = input("Email -> ")
            elif opcion == 0:
                print("Regresando.")
                iofile.modificar_registro(self.lista_usuarios, "usuarios")
                break
            else: print("Opcion invalida.")
                
            

        
        

    def sesion_iniciada(self,):
        
        try:    lista_mascotas = iofile.lectura_fichero_lista("mascotas")
        except FileNotFoundError:   lista_mascotas = []

        gestion_mascotas = Gestion_mascotas(lista_mascotas, self.usuario_actual.usuario)
        
        
        while True:
            menu.menu_titulo()
            menu.menu_sesion_iniciada(self.usuario_actual.nombre)
        
            try: opcion = int(menu.opcion_menu)
            except Exception as e: 
                print(f"Error, {e}.")
                opcion = None
        
            if opcion == 1: pass
            elif opcion == 2: pass
            elif opcion == 3: gestion_mascotas.inicio()
            elif opcion == 4: self.actualizar_perfil()
            elif opcion == 0:
                print("Regresando.")
                self.usuario_actual = None
                break
            else: print("Error, opcionion invalida")
                
        

    def iniciar_sesion(self):
        if len(self.lista_usuarios) > 0 :
            user = input("User -> ")
            password = input("Password -> ")
            
            for u in self.lista_usuarios:
                if u.usuario == user and u.password == password:
                    self.usuario_actual = u
                    self.sesion_iniciada()
                else:
                    print("Error, usuario y/o contraseña invalidos.")
    
        else:
            print("Error, lista de usuarios vacia")
            
    def registrar_usuario(self,):
        user = input("User -> ")
        nombre = input("Nombre -> ")
        password = input("Password = > ")
        genero = input("Genero -> ")
        telefono = input("Telefono -> ")
        email = input("Email -> ")
    
        usuario = Usuario(user, nombre, password, genero, telefono, email)
        self.lista_usuarios.append(usuario)
        iofile.escritura_fichero_registro(usuario, "usuarios")

    def buscar_usuario(self,):
        if len(self.lista_usuarios)>0:
            user = input("Usuario a buscar -> ")

            for u in self.lista_usuarios: 
                if u.usuario == user:
                    print(str(u))
                else:
                    print("Error, no existe el usuario buscado.")
        else:
            print("Error, lista de usuario vacia")

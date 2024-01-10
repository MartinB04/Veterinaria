from Usuario import *
from Menu import *
from IOFile import *
from Mascota import *

menu = Menu()
#opcion = None
lista_mascotas = []
#lista_usuarios = []
usuario_actual = None
iofile = IOFile()

try: lista_usuarios = iofile.lectura_fichero_lista("usuarios")
except FileNotFoundError: lista_usuarios = []

def buscar_mascotas():
    for mascota in lista_mascotas:
        if(mascota.dueño == usuario_actual.usuario):
            return True
        else:
            return False

def buscar_mascota(usuario_actual, nombre_mascota):
    mascota_modificada = None
    for mascota in lista_mascotas:
        if usuario_actual.usuario == mascota.dueño and mascota.nombre == nombre_mascota:
            mascota_modificada = mascota
        return mascota_modificada


def actualizar_perfil_mascota(usuario_actual):
    nombre_mascota = input("Mascota a modificar -> ")
    mascota_modificada = buscar_mascota(usuario_actual, nombre_mascota)
    opcion = None
    
    if mascota_modificada:
        while True:
            menu.menu_titulo
            menu.menu_actualizar_perfil_mascota()
            
            try: opcion = menu.opcionion_menu
            except Exception as e: print(f"Error, {e}.")
            
            if opcion == 1: mascota_modificada.nombre = input("Nombre -> ")
            elif opcion == 2: mascota_modificada.tipo_mascota = input("Tipo de mascota -> ")
            elif opcion == 3: mascota_modificada.raza = input("Raza -> ")
            elif opcion == 4: mascota_modificada.peso = input("Peso -> ")
            elif opcion == 5: mascota_modificada.genero = input("Genero -> ")
            elif opcion == 6: mascota_modificada.color = input("Color -> ")
            elif opcion == 7: mascota_modificada.fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa) -> ")
            elif opcion == 0:
                print("Regresando.")
                break
            else: print("Error, opcionion fuera de rango.")
                    
            iofile.modificar_registro(lista_mascotas, "mascotas")
                          
    else: print("Error, mascota no registrada.")   
    

def registrar_mascota(usuario_actual):
    
    print("<----- Registro de Mascotas ----->")
    
    nombre = input("Nombre -> ")
    tipo_mascota = input("Tipo de mascota -> ")
    raza = input("Raza -> ")
    genero = input ("Genero -> ")
    fecha_nacimiento = input("Fecha de nacimiento -> ")
    peso = input("Peso -> ")
    color = input("Color -> ")

    mascota = Mascota(nombre, usuario_actual.usuario, tipo_mascota, raza, genero, fecha_nacimiento, peso, color)
    lista_mascotas.append(mascota)
    iofile.escritura_fichero_registro(mascota, "mascotas")
    
def mis_mascotas(usuario_actual):
    if buscar_mascotas(usuario_actual): 
        for i, mascota in enumerate(lista_mascotas, start=1):
            if(mascota.dueño == usuario_actual.usuario):
                print(f"\nMascota #{i}")
                print(str(mascota))
    else:
        print("Error, no tienes mascotas registradas")
        

def mascotas(usuario_actual):
    while True:
        menu.menu_titulo()
        menu.menu_mascotas()
        try: opcion = menu.opcionion_menu
        except Exception as e: print(f"Error, {e}.")
        
        if opcion == 1: mis_mascotas(usuario_actual)
        elif opcion == 2: registrar_mascota(usuario_actual)
        elif opcion == 3: actualizar_perfil_mascota(usuario_actual)
        elif opcion == 4: pass
        elif opcion == 0:
            print("Error, opcionion fuera de rango.")
            break
        else: print("Error, opcion invalida.")
            
            
def actualizar_perfil(usuario_actual):
    
    while True:
        
        menu.menu_titulo()
        menu.menu_acutalizar_perfil_usuario()
        try: opcion = int(menu.opcionion_menu)
        except Exception as e: print(f"Error, {e}.")
        
        if opcion == 1: usuario_actual.usuario = input("User -> ")
        elif opcion == 2: usuario_actual.nombre = input("Nombre -> ")
        elif opcion == 3: usuario_actual.password = input("Password -> ")
        elif opcion == 4: usuario_actual.genero = input("Genero -> ")
        elif opcion == 5: usuario_actual.telefono = input("Telefono -> ")
        elif opcion == 6: usuario_actual.email = input("Email -> ")
        elif opcion == 0:
            print("Regresando.")
            break
        else: print("Opcionopcionion invalida.")
                
        iofile.modificar_registro(lista_usuarios, "usuarios")

        
        

def sesion_iniciada(usuario_actual):
    while True:
        menu.menu_titulo()
        menu.menu_sesion_iniciada(usuario_actual.nombre)
        
        try: opcion = int(menu.opcionion_menu)
        except Exception as e: print(f"Error, {e}.")
        
        if opcion == 1: pass
        elif opcion ==2 : pass
        elif opcion == 3: mascotas(usuario_actual)
        elif opcion ==4 : actualizar_perfil(usuario_actual)
        elif opcion == 0:
            print("Regresando.")
            break
        else: print("Error, opcionion invalida")
                
        

def iniciar_sesion():
    if len(lista_usuarios) > 0 :
        user = input("User -> ")
        password = input("Password -> ")
            
        for u in lista_usuarios:
            if u.usuario == user and u.password == password:
                usuario_actual = u
                sesion_iniciada(usuario_actual)
            else:
                print("Error, usuario y/o contraseña invalidos.")
    
    else:
        print("Error, lista de usuarios vacia")
            
def registrar_usuario():
    user = input("User -> ")
    nombre = input("Nombre -> ")
    password = input("Password = > ")
    genero = input("Genero -> ")
    telefono = input("Telefono -> ")
    email = input("Email -> ")
    
    usuario = Usuario(user, nombre, password, genero, telefono, email)
    lista_usuarios.append(usuario)
    iofile.escritura_fichero_registro(usuario, "usuarios")

def buscar_usuario():
    if len(lista_usuarios)>0:
        user = input("Usuario a buscar -> ")

        for u in lista_usuarios: 
            if u.usuario == user:
                print(str(u))
            else:
                print("Error, no existe el usuario buscado.")
    else:
        print("Error, lista de usuario vacia")     
        
while(True):
    menu.menu_titulo()
    menu.menu_principal()
    
    try: opcion = int(menu.opcionion_menu)
    except Exception as e: print(f"Error, {e}.")
    
    if opcion == 1: iniciar_sesion()
    elif opcion == 2: registrar_usuario()
    elif opcion == 3 : buscar_usuario()
    elif opcion == 0 : 
        print("Saliendo.")
        break
    else: print("Opcionopcionion invalida.")
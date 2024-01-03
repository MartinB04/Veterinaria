from Usuario import *
from Menu import *
from IOFile import *
from Mascota import *

menu = Menu()
opc = None
lista_mascotas = []
lista_usuarios = []
usuario_actual = None
iofile = IOFile()

try:
    lista_usuarios = iofile.lectura_fichero_lista("usuarios")
except: pass

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
    opc_aux = None
    
    if mascota_modificada:
        while True:
            try:
                menu.menu_titulo
                menu.menu_actualizar_perfil_mascota()
                opc_aux = menu.opc
                
                match opc_aux:
                    case 1: mascota_modificada.nombre = input("Nombre -> ")
                    case 2: mascota_modificada.tipo_mascota = input("Tipo de mascota -> ")
                    case 3: mascota_modificada.raza = input("Raza -> ")
                    case 4: mascota_modificada.peso = input("Peso -> ")
                    case 5: mascota_modificada.genero = input("Genero -> ")
                    case 6: mascota_modificada.color = input("Color -> ")
                    case 7: mascota_modificada.fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa) -> ")
                    case 0: 
                        print("Regresando.")
                        break
                    case _: print("Error, opcion fuera de rango.")
                    
                iofile.modificar_registro(lista_mascotas, "mascotas")
                        
            except: print("Error, opcion invalida.")
            
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
        try:
            menu.menu_titulo()
            menu.menu_mascotas()
            opc_aux = menu.opc
        
            match opc_aux:
                case 1: mis_mascotas(usuario_actual)
                case 2: registrar_mascota(usuario_actual)
                case 3: actualizar_perfil_mascota(usuario_actual)
                case 4: pass
                case 0:
                    print("Error, opcion fuera de rango.")
                    break
                case _: print("Error, opcion fuera de rango.")
                
        except: print("Error, opcion invalida.")

def actualizar_perfil(usuario_actual):
    
    while True:
        try:
            menu.menu_titulo()
            menu.menu_acutalizar_perfil_usuario()
            opc_aux = menu.opc
        
            match opc_aux:
                case 1: usuario_actual.usuario = input("User -> ")
                case 2: usuario_actual.nombre = input("Nombre -> ")
                case 3: usuario_actual.password = input("Password -> ")
                case 4: usuario_actual.genero = input("Genero -> ")
                case 5: usuario_actual.telefono = input("Telefono -> ")
                case 6: usuario_actual.email = input("Email -> ")
                case 0: 
                    print("Regresando.")
                    break   
                case _: print("Error, opcion fuera de rango.")
                
            iofile.modificar_registro(lista_usuarios, "usuarios")

        
        except: print("Error, opcion invalida.")

def sesion_iniciada(usuario_actual):
    while True:
        try:
            menu.menu_titulo()
            menu.menu_sesion_iniciada(usuario_actual.nombre)
            opc_aux = menu.opc
            match opc_aux:
                case 1: pass
                case 2: pass
                case 3: mascotas(usuario_actual)
                case 4: actualizar_perfil(usuario_actual)
                case 0: 
                    print("Cerrando sesion.")
                    break
                case _: print("Error, opcion fuera de rango.")
                
        except: print("Error, opcion invalida.")

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
    try:
        menu.menu_titulo()
        menu.menu_principal()
        opc = menu.opc
    
        match(opc):
            case 1: iniciar_sesion()
            case 2: registrar_usuario()
            case 3: buscar_usuario()
            case 0: 
                print("Saliendo del programa.")
                break
            case _: print("Error, opcion fuera de rango.")
                    
    except:
        print("Error, opcion invalida.")
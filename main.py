from Usuario import *
from Menu import *
from IOFile import *

menu = Menu()
opc = None
lista_usuarios = []
usuario_actual = None
iofile = IOFile()

def modificar_perfil(usuario_actual):    
    while True:
        menu.menu_titulo()
        menu.menu_modificar_perfil()
        opc_aux = menu.opc
        value = None
        
        match opc_aux:

            case 1:
                value = input("User -> ")
                usuario_actual.usuario = value
                
            case 2:
                value = input("Nombre -> ")
                usuario_actual.nombre = value
                
            case 3:
                value = input("Password -> ")
                usuario_actual.password = value
                
            case 4:
                value = input("Genero -> ")
                usuario_actual.genero = value
                
            case 5:
                value = input("Telefono -> ")
                usuario_actual.telefono = value
                
            case 6:
                value = input("Email -> ")
                usuario_actual.email = value
                
        iofile.modificar_usuario(lista_usuarios)

        if opc_aux == 0:
            break

def sesion_iniciada(usuario_actual):
    while True:
        menu.menu_titulo()
        menu.menu_sesion_iniciada(usuario_actual.nombre)
        opc_aux = menu.opc
        match opc_aux:
            case 1:
                pass
            case 2:
                pass
            case 3:
                modificar_perfil(usuario_actual)
            
        if opc_aux == 0:
            break

def iniciar_sesion():
    if len(lista_usuarios) > 0 :
        user = input("User -> ")
        password = input("Password -> ")
            
        for u in lista_usuarios:
            print(u.usuario) 
            if u.usuario == user and u.password == password:
                usuario_actual = u
                sesion_iniciada(usuario_actual)
            else:
                print("No existe el usuario ingresado.")
    
    else:
        print("Error, no hay lista_usuarios registrados")
            
def registrar_usuario():
    user = input("User -> ")
    nombre = input("Nombre -> ")
    password = input("Password = > ")
    genero = input("Genero -> ")
    telefono = input("Telefono -> ")
    email = input("Email -> ")
    usuario = Usuario(user, nombre, password, genero, telefono, email)
    lista_usuarios.append(usuario)
    print(str(usuario))
    iofile.escritura_registro(usuario)

def buscar_usuario():
    if len(lista_usuarios)>0:
        user = input("User a buscar -> ")

        for u in lista_usuarios: 
            if u.usuario == user:
                print(str(u))
            else:
                print("No existe el usuario ingresado.")
    else:
        print("Error, no hay lista_usuarios registrados")     
        

lista_usuarios = iofile.lectura_usuarios()

while(True):
    menu.menu_titulo()
    menu.menu_principal()
    opc = menu.opc
    
    match(opc):
        case 1: iniciar_sesion()
            
        case 2: registrar_usuario()
            
        case 3: buscar_usuario()
            
    if(opc == 0):
        break
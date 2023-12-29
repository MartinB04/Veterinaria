from Usuario import *
from Menu import *
from IOFile import *
from Mascota import *

menu = Menu()
opc = None
lista_usuarios = []
lista_mascotas = []
usuario_actual = None
iofile = IOFile()

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
    print(str(mascota))
    lista_mascotas.append(mascota)
    iofile.escritura_fichero_registro(mascota, "mascotas")
    
def mis_mascotas(usuario_actual):

    if cargar_mascotas_usuario(usuario_actual):
        
        for i, mascota in enumerate(lista_mascotas, start=1):
            if(mascota.dueño == usuario_actual.usuario):
                print(f"\nMascota #{i}")
                print(str(mascota))
    
    else:
        print("Error, no tienes mascotas registradas")
        
def cargar_mascotas_usuario(usuario_actual):
    for m in lista_mascotas:
        if(m.dueño == usuario_actual.usuario):
            return True
    else:
        return False

def mascotas(usuario_actual):
    while True:
        menu.menu_titulo()
        menu.menu_mascotas()
        opc_aux = menu.opc
        
        match opc_aux:
            case 1:
                mis_mascotas(usuario_actual)
            case 2:
                registrar_mascota(usuario_actual)
            case 3:
                pass
            case 4:
                pass
        
        if opc_aux == 0:
            break

def actualizar_perfil(usuario_actual):    
    while True:
        menu.menu_titulo()
        menu.menu_acutalizar_perfil_usuario()
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
                
        iofile.modificar_registro(lista_usuarios, "usuarios")

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
                mascotas(usuario_actual)
            case 4: 
                actualizar_perfil(usuario_actual)
                
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
    iofile.escritura_fichero_registro(usuario, "usuarios")

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
        

lista_usuarios = iofile.lectura_fichero_lista("usuarios")

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
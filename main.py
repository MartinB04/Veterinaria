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
    #print(str(mascota))
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
        try:
            menu.menu_titulo()
            menu.menu_mascotas()
            opc_aux = menu.opc
        
            match opc_aux:
                case 1: mis_mascotas(usuario_actual)
                case 2: registrar_mascota(usuario_actual)
                case 3: pass
                case 4: pass
                case 0:
                    print("Error, opcion fuera de rango.")
                    break
                case _: print("Error, opcion fuera de rango.")
                
        #if opc_aux == 0:
            #break
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

            #if opc_aux == 0:
                #break
        
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
                
            #if opc_aux == 0:
                #break
        except: print("Error, opcion invalida.")

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
    #print(str(usuario))
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
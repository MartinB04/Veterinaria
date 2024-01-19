from Usuario import *
from Menu import *
from IOFile import *
from Mascota import *
from Gestion_usuarios import *

menu = Menu()
iofile = IOFile()

try: 
    lista_usuarios = iofile.lectura_fichero_lista("usuarios")
    print("Lista con registros")
except FileNotFoundError: 
    lista_usuarios = []
    print("Lista vacia")

gestion_usuarios = Gestion_usuarios(lista_usuarios)

while(True):
    menu.menu_titulo()
    menu.menu_principal()
    
    try: opcion = int(menu.opcion_menu)
    except Exception as e: 
        print(f"Error, {e}.")
        opcion = None
    
    if opcion == 1: gestion_usuarios.iniciar_sesion()
    elif opcion == 2: gestion_usuarios.registrar_usuario()
    elif opcion == 3: gestion_usuarios.buscar_usuario()
    elif opcion == 0: 
        print("Saliendo.")
        break
    else: print("Opcion invalida.")
    
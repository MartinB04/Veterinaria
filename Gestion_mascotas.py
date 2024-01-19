from Menu import *
from Mascota import *
from IOFile import *

#mascota = Mascota()
menu = Menu()
iofile = IOFile()

class Gestion_mascotas:
    
    lista_mascotas = None
    dueño_actual = None
    
    
    def __init__(self, lista, nombre) -> None:
        self.lista_mascotas = lista
        self.dueño_actual = nombre
        
    '''    
    def buscar_mascotas(self,):
        for mascota in self.lista_mascotas:
            if(mascota.dueño == self.dueño_actual):
                return True
            else:
                return False
                
    def buscar_mascota(self, nombre_mascota, *args):
        mascota_modificada = None
        for mascota in self.lista_mascotas:
            if self.dueño_actual== mascota.dueño and mascota.nombre == nombre_mascota:
                mascota_modificada = mascota
            return mascota_modificada
    '''
            
    def buscar_mascotas(self, *args):
        if(len(args) == 1):
            mascota_buscada = None
            for mascota in self.lista_mascotas:
                if self.dueño_actual== mascota.dueño and mascota.nombre == args[0]:
                    mascota_buscada = mascota
                return mascota_buscada
        else:
            for mascota in self.lista_mascotas:
                if(mascota.dueño == self.dueño_actual): 
                    return True
            return False    


    def actualizar_perfil_mascota(self,):
        if not self.buscar_mascotas():
            print ("Error, no tienes mascotas registradas")
        else:
            nombre_mascota = input("Mascota a modificar -> ")
            mascota_buscada = self.buscar_mascotas(nombre_mascota)
    
            if mascota_buscada == False:
                print("Error, mascota no registrada.")
            else: 
                while True:
                    menu.menu_titulo
                    menu.menu_actualizar_perfil_mascota()
            
                    try: opcion = int(menu.opcion_menu)
                    except Exception as e: 
                        print(f"Error, opcion invalida")
                        opcion = None
            
                    if opcion == 1: mascota_buscada.nombre = input("Nombre -> ")
                    elif opcion == 2: mascota_buscada.tipo_mascota = input("Tipo de mascota -> ")
                    elif opcion == 3: mascota_buscada.raza = input("Raza -> ")
                    elif opcion == 4: mascota_buscada.peso = input("Peso -> ")
                    elif opcion == 5: mascota_buscada.genero = input("Genero -> ")
                    elif opcion == 6: mascota_buscada.color = input("Color -> ")
                    elif opcion == 7: mascota_buscada.fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa) -> ")
                    elif opcion == 0:
                        print("Regresando.")
                        iofile.modificar_registro(self.lista_mascotas, "mascotas")
                        break
                    else: print("Error, opcionion fuera de rango.")
                    
    def registrar_mascota(self,):
    
        print("<----- Registro de Mascotas ----->")
    
        nombre = input("Nombre -> ")
        tipo_mascota = input("Tipo de mascota -> ")
        raza = input("Raza -> ")
        genero = input ("Genero -> ")
        fecha_nacimiento = input("Fecha de nacimiento -> ")
        peso = input("Peso -> ")
        color = input("Color -> ")

        mascota = Mascota(nombre, self.dueño_actual, tipo_mascota, raza, genero, fecha_nacimiento, peso, color)
        self.lista_mascotas.append(mascota)
        iofile.escritura_fichero_registro(mascota, "mascotas")
    
    def mis_mascotas(self,):
        if self.buscar_mascotas(): 
            for i, mascota in enumerate(self.lista_mascotas, start=1):
                if(mascota.dueño == self.dueño_actual):
                    print(f"\nMascota #{i}")
                    print(str(mascota))
        else:
            print("Error, no tienes mascotas registradas")
        

    def inicio(self,):
        while True:
            menu.menu_titulo()
            menu.menu_mascotas()
            try: opcion = int(menu.opcion_menu)
            except ValueError as e: 
                print(f"Error, {e}.")
                opcion = None
        
            if opcion == 1: self.mis_mascotas()
            elif opcion == 2: self.registrar_mascota()
            elif opcion == 3: self.actualizar_perfil_mascota()
            elif opcion == 4: pass
            elif opcion == 0:
                print("Error, opcionion fuera de rango.")
                break
            else: print("Error, opcion invalida.")
import csv
import os

from Usuario import *
from Mascota import *

class IOFile:
    
    _extension = ".csv"
    #ruta_usuarios = "usuarios.csv"
    _directorio = "csv/"
    
    def __init__(self) -> None:
        pass
    
    def escritura_fichero_registro(self, nuevo_registro, fichero):
        with open(self._directorio + fichero + self._extension, "a", newline="\n") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow(nuevo_registro.to_tuple())
    
    def escritura_fichero_lista(self, lista_registros, fichero):
        with open(self._directorio  + fichero + self._extension, "w", newline="\n") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            for registro in lista_registros:
                writer.writerow(registro.to_tuple()) #escribre la tupla que contiene los datos del usuario
    
    def lectura_fichero_lista(self, fichero):
        lista_registros = []
        with open(self._directorio  + fichero + self._extension, newline="\n") as csvfile:
            self.lector = csv.reader(csvfile, delimiter=",")
            if(fichero == "usuarios"):
                for usuario, nombre, password, genero, telefono, email in self.lector:
                    lista_registros.append(Usuario(usuario, nombre, password, genero, telefono, email))
            elif(fichero == "mascotas"):
                for nombre, dueño, fecha_nacimiento, tipo_mascota, raza, peso, genero, color in self.lector:
                    lista_registros.append(Mascota(nombre, dueño, fecha_nacimiento, tipo_mascota, raza, peso, genero, color))
            return lista_registros
        
    def modificar_registro(self, lista_registros, fichero):
        self.eliminar_fichero_csv(fichero)
        self.escritura_fichero_lista(lista_registros, fichero)

    def eliminar_fichero_csv(self, fichero):
        try:
            os.remove(self._directorio +fichero+ self._extension)
        except FileNotFoundError:
            print(f"Error, {fichero + self._extension} no encontrado.")
 
    
'''
contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

with open("contactos.csv", "w", newline="\n") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for contacto in contactos:
        writer.writerow(contacto)
'''

'''
with open("contactos.csv", newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for nombre, empleo, email in reader:
        print(nombre, empleo, email)
        '''
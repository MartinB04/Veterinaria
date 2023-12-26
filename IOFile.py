import csv
from Usuario import *
import os

class IOFile:
    
    ruta_usuarios = "usuarios.csv"
    directorio = "csv/"
    
    def __init__(self) -> None:
        pass
    
    def escritura_usuarios(self, lista_usuarios):
        with open(self.directorio + self.ruta_usuarios, "w", newline="\n") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            for usuario in lista_usuarios:
                writer.writerow(usuario.to_tuple()) #escribre la tupla que contiene los datos del usuario
    
    def lectura_usuarios(self):
        lista_usuarios = []
        with open(self.directorio + self.ruta_usuarios, newline="\n") as csvfile:
            self.lector = csv.reader(csvfile, delimiter=",")
            for usuarios, nombre, password, genero, telefono, email in self.lector:
                lista_usuarios.append(Usuario(usuarios, nombre, password, genero, telefono, email))
            return lista_usuarios

    def modificar_usuario(self, lista_usuarios):
        self.eliminar_archivo_csv()
        self.escritura_usuarios(lista_usuarios)

    def eliminar_archivo_csv(self):
        try:
            os.remove(self.directorio + self.ruta_usuarios)
        except FileNotFoundError:
            print(f"Error, {self.ruta_usuarios} no encontrado.")
 
    
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
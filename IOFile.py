import csv

class IOFile:
    
    ruta_usuarios = "usuarios.csv"
    lector = None
    
    def __init__(self) -> None:
        pass
    
    def escritura_usuarios(self, usuarios):
        with open(self.ruta_usuarios, "w", newline="\n") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            for u in usuarios:
                writer.writerow(u.to_tuple())
    
    def lectura_usuarios(self):
        with open(self.ruta_usuarios, newline="\n") as csvfile:
            self.lector = csv.reader(csvfile, delimiter=",")
            for nombre, empleo, email in self.lector:
                print(nombre, empleo, email)

    @property
    def lector(self):
        return self.lector
    
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
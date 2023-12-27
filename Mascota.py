class Mascota:
    _nombre = None
    _dueño = None
    _fecha_nacimiento = None
    _tipo_mascota = None
    _raza = None
    _peso = None
    _genero = None
    _color = None
    
    def __init__(self, nombre, dueño, tipo_mascota, raza, genero, fecha_nacimiento, peso, color) -> None:
        self._nombre = nombre
        self._dueño = dueño
        self._fecha_nacimiento = fecha_nacimiento
        self._tipo_mascota = tipo_mascota
        self._raza = raza
        self._peso = peso
        self._genero = genero
        self._color = color
        
    def __str__(self):
        return f"Nombre -> {self._nombre}\nDueño -> {self._dueño}\nTipo de mascota -> {self._tipo_mascota}\nRaza -> {self._raza}\nGenero -> {self._genero}\nFecha de nacimiento -> {self._fecha_nacimiento}\nPeso -> {self._peso}\nColor -> {self._color}"
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
        
    @property
    def dueño(self):
        return self._dueño
    
    @dueño.setter
    def dueño(self, value):
        self._dueño = value
        
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        self._fecha_nacimiento = value
        
    @property
    def tipo_mascota(self):
        return self._tipo_mascota
    
    @tipo_mascota.setter
    def tipo_mascota(self, value):
        self._tipo_mascota = value
        
    @property
    def raza(self):
        return self._raza
    
    @raza.setter
    def raza(self, value):
        self._raza = value
        
    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, value):
        self._peso = value
        
    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, value):
        self._genero = value
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value
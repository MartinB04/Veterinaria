class Mascota:
    _nombre = None
    _dueño = None
    _fecha_nacimiento = None
    _tipo_mascota = None
    _raza = None
    _peso = None
    _genero = None
    _color = None
    
    def __init__(self, nombre, dueño, fecha_nacimiento, tipo_mascota, raza, peso, genero, color) -> None:
        _nombre = nombre
        _dueño = dueño
        _fecha_nacimiento = fecha_nacimiento
        _tipo_mascota = tipo_mascota
        _raza = raza
        _peso = peso
        _genero = genero
        _color = color
        
    
    
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
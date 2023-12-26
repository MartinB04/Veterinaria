class Usuario:
    _nombre = ""
    _usuario = ""
    _password = ""
    _genero = ""
    _email = ""
    _telefono = ""
        
    
    def __init__(self, nombre, usuario, password, genero, email, telefono) -> None:
        self._nombre = nombre
        self._usuario = usuario
        self._password = password
        self._genero = genero
        self._email = email
        self._telefono = telefono
        
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
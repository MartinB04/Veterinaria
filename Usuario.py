class Usuario:
    _nombre = ""
    _usuario = ""
    _password = ""
    _genero = ""
    _email = ""
    _telefono = ""
        
    
    def __init__(self, usuario, nombre, password, genero, email, telefono) -> None:
        self._usuario = usuario
        self._nombre = nombre
        self._password = password
        self._genero = genero
        self._email = email
        self._telefono = telefono
        
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
        
    @property
    def usuario(self):
        return self._usuario
    
    @usuario.setter
    def usuario(self, value):
        self._usuario = value
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = value
        
    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, value):
        self._genero = value
        
    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, value):
        self._telefono = value
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value
    
    def __str__(self) -> str:
        return f"User -> {self._usuario}\nNombre ->{self._nombre}\nPassword -> {self._password}\nGenero -> {self._genero}\nTelefono -> {self._telefono}\nEmail -> {self._email}"
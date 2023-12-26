class Menu:
    _opc = ""
    
    def __init__(self) -> None:
        pass
    
    
    
    def menu_principal(self):
        print("<----- Veterinaria ----->")
        print("<----- Menu Principal ----->\n\n")
        print("1. Iniciar sesion.")
        print("2. Registrar usuario.")
        print("0. Cerrar sesion.")
        self._opc = (input("Opc -> "))
        
    @property
    def opc(self):
        return self._opc
        
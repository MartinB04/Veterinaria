from Usuario import *
from Menu import *




menu = Menu()
opc = None
while(True):
    menu.menu_principal
    opc = menu.opc()
    
    match(opc):
        case 1:
            pass
        case 2: 
            pass
    
    if(opc == 0):
        break
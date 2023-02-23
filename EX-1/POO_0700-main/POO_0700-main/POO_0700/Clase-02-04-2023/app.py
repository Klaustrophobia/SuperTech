# from Classes import Casa #
from Classes import *

#THE METHOD IS DEFINED BY DEF#
def main():
    cliente = Cliente(1, 'Velvet')
    casa = Casa(2, 100, cliente)
    casa.info_casa()
    print(cliente.casas[0].numero)
    cliente.mis_metros_cuadrados(2) 
 #THIS IS THE INSTANCE OF THE FUNCTION MAIN#
    
#THE STRUCTURE "IF" HAS TO BE AT THE LEVEL OF THE DEF #
if __name__ == '__main__':
        main()
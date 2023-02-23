
class Cliente:
    
    def __init__(self, id,  nombre):
        self.id = id
        self.nombre = nombre
        #DEFINITION OF ARRAYS ON PYTHON#
        self.casas = {}
        
    
    def mis_metros_cuadrados(self, numero_casa):
        
        # encontro = False        
        # Definition of how to identify the "Casas" #
        
        # for casa in self.casas:
        #    if casa.numero == numero_casa:
        #        encontro = True
        #        print ('Metros cuadradados de casa {0}: {1} mts2' .format(numero_casa, casa.metrosConstruccion))
        #        break
            
        #if not encontro:
        #   print ('ID no encontrado')    
        
        print( self.casas[numero_casa].metrosConstruccion )

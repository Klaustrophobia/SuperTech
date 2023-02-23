from Classes import Cliente

class Casa:

    def __init__(self, numero, metrosConstruccion, cliente):
        self.numero = numero                                #Un atributo con dos "_" se convierte en atributo privado #
        self.metrosConstruccion = metrosConstruccion
        self.cliente = cliente
        self.cliente.casas[self.numero] = self
        print('Casa objeto instanciado')
        

    def info_casa(self):
        print('La casa con numero {0}, tiene duenio {1}'. format(self.numero, self.cliente.nombre))
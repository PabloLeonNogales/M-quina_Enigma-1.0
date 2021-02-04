from piezas import *

class Reflector():

    def __init__(self, abecedario = ENGLISHDIC, reflector = ENGREFLECTORB):
        self.abecedario = abecedario
        self.reflector = reflector

    def __str__(self):
        cadena = 'Reflector' 
        return cadena

    # Función que refleja una posición (de P0 a P1). Notar que, como el reflector
    # está ordenado, se elige el par que ocupa la posición 'posicion' y devuelve su reflejo.
    # Hay que acordarse de cómo definir esta posición en la máquina (ahora mismo, 
    # la posición 4 es, por ejemplo, el par quinto, por la nomenclatura de Python).
    def refleja(self, posicion):
        return self.reflector[posicion][1]

if __name__ == '__main__':

    s = Reflector()
    print(s.reflector)
    print(s.refleja(4))
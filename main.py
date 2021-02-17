# Definitivamente, vamos a unir el engranaje de rotores al reflector, para generar la máquina enigma. 
# Por esta razón, llamo a este archivo main.py

# En caso de trabajar con una ventana gráfica n vez de con consola, este sería el archivo de gestión de gráficos.

from ClassRotor import *
from ClassReflector import *
from piezas import *
from ClassEngranaje import *

class Enigma():

    def __init__(self, reflector, *rotores):

        if type(reflector) != Reflector: 
            raise ValueError('Fatal error. No ha introducido un objeto Reflector')
        self.engranaje = Engranaje(*rotores)
        self.reflector = reflector
        self.nrotores = (self.engranaje.lenRotores)
        
    def enigmaCodifica(self, letra):
        codi = self.engranaje.codiEngranaje(letra)
        pos = self.engranaje.rotores[self.nrotores-1].posicionLetraC(codi)
        reflejo = self.reflector.refleja(pos)
        letra = self.engranaje.rotores[self.nrotores-1].letraPosicionC(reflejo)
        return self.engranaje.decodiEngranaje(letra)


if __name__ == '__main__':

    r1 = Rotor(rotor = ENGROTOR1)
    r2 = Rotor(rotor = ENGROTOR2)
    r3 = Rotor(rotor = ENGROTOR3, letraInicial = 'Y')
    r4 = Rotor(rotor = ENGROTOR4)
    r5 = Rotor(rotor = ENGROTOR5)
    s1 = Reflector(reflector=ENGREFLECTORB)

    rr=Enigma(s1,r3,r2,r1)
    print(r3.iRotor)

    letra = input('¿Qué letra o frase (sin espacios) quieres pulsar? ')
    for n in letra:
        print(rr.enigmaCodifica(n))

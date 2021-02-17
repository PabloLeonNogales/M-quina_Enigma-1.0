# Esta es la máquina, es decir, va a juntar rotores y reflectores y nos dará la solución
# 
# Definimos la clase Enigma, para irle incorporando atributos y métodos propios 

from ClassRotor import *
from ClassReflector import *
from piezas import *

# Una Clase para definir la combinación de rotores y las llamadas entre ellos
class Engranaje():
    
    def __init__(self,*rots): 
        self.rotores = []
        self.contadores = []
        for n in rots:
            if type(n) == Rotor: 
                self.rotores.append(n)
            else:
                print('El objeto {} no es un objeto Rotor. Se eliminará del objeto Engranaje'.format(n))
        self.lenRotores = len(self.rotores)
        for i in range(1, self.lenRotores):
            if self.rotores[i].abecedario != self.rotores[0].abecedario:
                raise ValueError('Fatal error. Los rotores no son del mismo diccionario')
        self.lendic = len(self.rotores[0].abecedario)
        for i in range(self.lenRotores):
            self.contadores.append(self.rotores[i].iRotor)
    
    # Esta función comprobará si el avance del primer rotor provoca avances en el resto.
    # Esta función no actua en el primer rotor, porque este siempre se mueve. Por tanto, 
    # empieza en el segundo rotor (rotores[1]). Si el rotor anterior llegó a longdic 
    # (la longitud del abecedario), lo reinicia y avanza el rotor actual.
    def controlAvance(self):
        for i in range(1, self.lenRotores):
            if self.rotores[i-1].iRotor == self.lendic:
                self.rotores[i-1].iRotor = 0
                self.rotores[i].avanza()
    
    # Esta función realiza el codificado de todo el engranaje, tenga los rotores que tenga. 
    # Entra un letra y sale otra para el reflector.
    def codiEngranaje(self, letra):
        self.rotores[0].avanza()
        if self.lenRotores > 1:
            self.controlAvance()
        for i in range(0, self.lenRotores):
            a = self.rotores[i].codifica(letra)
            pos = self.rotores[i].posicionLetraC(a)
            letra = self.rotores[i].abecedario[pos]
        return a

    # Esta función realiza el decodificado de todo el engranaje, tenga los rotores que tenga. 
    # Entra un letra desde el reflector y sale otra para iluminar la bombilla.
    def decodiEngranaje(self, letra):
        for i in range((self.lenRotores-1), -1, -1):
            a = self.rotores[i].decodifica(letra)
            pos = self.rotores[i].posicionLetraC(a)
            try:
                letra = self.rotores[i-1].letraPosicionC(pos)
            except:
                pass
        return a



if __name__ == '__main__':

    r1 = Rotor(rotor = ENGROTOR1)
    r2 = Rotor(rotor = ENGROTOR2)
    r3 = Rotor(rotor = ENGROTOR3, letraInicial = 'Y')
    r4 = Rotor(rotor = ENGROTOR4)
    r5 = Rotor(rotor = ENGROTOR5)
    s1 = Reflector(reflector=ENGREFLECTORB)

    rr=Engranaje(r3, r2)
    letra = input('¿Qué letra o frase (sin espacios) quieres codificar? ')
    for i in letra:
        print (rr.codiEngranaje(i))
        print (r3.iRotor)
    letra = input('¿Qué letra o frase (sin espacios) quieres decodificar? ')
    for i in letra:
        print (rr.decodiEngranaje(i))
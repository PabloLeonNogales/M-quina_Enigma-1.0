from piezas import *

class Rotor():

    def __init__(self, abecedario = ENGLISHDIC, rotor = ENGROTOR3, letraInicial = 'A'):
        
        self.abecedario = abecedario
        self.pos0  = [n for n in range(len(abecedario))]        # Pos0 Fija
        self.rotor = rotor                                      # Rotor Fijo
        self.letraInicial = letraInicial
        self.pos0C = self.pos0[:]                               # Pos0 en movimiento
        self.rotorC = self.rotor[:]                             # Rotor en movimiento
        if letraInicial != 'A':
            self.posicionInicial(self.letraInicial)   
        self.iRotor = 0
    
    def __str__(self):
        cadena = 'Rotor' 
        return cadena

    # Como un rotor puede iniciar en cualquier posición (es móvil), 
    # definimos esta función para poder situarlo en dicha posición.
    # Recordar que debemos redefinir los coder/decoder.
    def posicionInicial(self, letra):
        value = self.abecedario.index(letra)
        self.rotorC = self.rotor[value:] + self.rotor[:value]
        self.pos0C = self.pos0[value:] + self.pos0[:value]

    # Cuando presionamos una tecla, el rotor avanza una posición. 
    # Esta función hace precisamente eso.
    # Recordar que debemos redefinir los coder/decoder.
    def avanza(self, paso = 1):
        self.rotorC = self.rotorC[paso:] + self.rotorC[:paso]    
        self.pos0C = self.pos0C[paso:] + self.pos0C[:paso]
        self.iRotor += paso

    # No está de más tener una función que retroceda:
    # Recordar que debemos redefinir los coder/decoder.
    def retrocede(self, paso = 1):
        n = len(self.rotorC)
        self.rotorC = self.rotorC[(n-paso):] + self.rotorC[:(n-paso)]    
        self.pos0C = self.pos0C[(n-paso):] + self.pos0C[:(n-paso)]
        self.iRotor -= paso

    # Proceso (método) de codificación
    def codifica(self,letra):
        numero = self.abecedario.index(letra)
        posCifrada = self.rotorC[numero]
        return  self.abecedario[posCifrada]
    
    # Proceso (método) de decodificación)
    def decodifica(self,letra):
        numero = self.abecedario.index(letra)
        poscifrada = self.rotorC.index(numero)
        return self.abecedario[poscifrada]

    # Proceso (método) para averiguar qué posición en el abecedario
    # ocupa actualmente una letra, porque el abecedario también va rotando...
    def posicionLetraC(self, letra):
        return self.pos0C.index(self.abecedario.index(letra))

    # Proceso (método) para ofrecer la letra que corresponde a una 
    # posición en la actualidad (con rotaciones o no)...
    def letraPosicionC(self, pos):
        return self.abecedario[self.pos0C[pos]]


if __name__ == '__main__':
    
    r = Rotor(letraInicial = 'H') 
    
    r.avanza(2)
    print(r.codifica('P'))
    print(r.decodifica('A'))

    r.retrocede(4)
    print(r.codifica('P'))
    print(r.decodifica('A'))

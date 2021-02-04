# Definición de Rotores y Reflectores Fijos. Al final, optaremos por esta opción para evitar 
# que los randoms nosmolesten a la hora de hacer pruebas. En todo caso, 
# podremos volver a los randoms cuando queramos

# Para los rotores y reflectores ingleses, uso el ejemplo gráfico de la máquina en el paquete de Pringles.

from random import *


ENGLISHDIC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ESPANOLDIC = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# ---------------------------------------
# ROTORES PARA DICCIONARIOS INGLESES:
# ---------------------------------------

ENGROTOR1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
ENGROTOR2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
ENGROTOR3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
ENGROTOR4 = [4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 1, 2, 12, 22, 3]
ENGROTOR5 = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]

# ---------------------------------------
# REFLECTORES PARA DICCIONARIOS INGLESES:
# ---------------------------------------

ENGREFLECTORB = [(0, 24), (1, 17), (2, 20), (3, 7), (4, 16), (5, 18), (6, 11), (7, 3), (8, 15), (9, 23), 
                 (10, 13), (11, 6), (12, 14), (13, 10), (14, 12), (15, 8), (16, 4), (17, 1), (18, 5), 
                 (19, 25), (20, 2), (21, 22), (22, 21), (23, 9), (24, 0), (25, 19)]
ENGREFLECTORC = [(0, 5), (1, 21), (2, 15), (3, 9), (4, 8), (5, 0), (6, 14), (7, 24), (8, 4), (9, 3), 
                 (10, 17), (11, 25), (12, 23), (13, 22), (14, 6), (15, 2), (16, 19), (17, 10), (18, 20), 
                 (19, 16), (20, 18), (21, 1), (22,13), (23, 12), (24, 7), (25, 11)]

# ---------------------------------------
# ROTORES PARA DICCIONARIOS ESPAÑOLES:
# ---------------------------------------

ESPROTOR1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9, 26]

# ---------------------------------------
# REFLECTORES PARA DICCIONARIOS ESPAÑOLES:
# ---------------------------------------

ESPREFLECTORB = [(0, 24), (1, 17), (2, 20), (3, 7), (4, 16), (5, 18), (6, 11), (7, 3), (8, 15), (9, 23), 
                 (10, 13), (11, 6), (12, 14), (13, 10), (14, 12), (15, 8), (16, 4), (17, 1), (18, 5), 
                 (19, 25), (20, 2), (21, 22), (22, 21), (23, 9), (24, 0), (25, 19), (26, 26)]



# También definiremos los generadores de rotores y reflectores, digamos que son las 'fábricas' que producen 
# esas piezas. Por si algún día queremos cambiar las especificaciones de los que tenemos, o crear nuevos a 
# partir de otros diccionarios... Son funciones, no clases. En realidad deberáin estar en sus respectivas 
# clases, pero lo coloco aquí para no ensuciar mucho el código que importa. 
 
def rotorAleatorio(abecedario = ENGLISHDIC):
    abecedario = abecedario
    rotor = [n for n in range(len(abecedario))]
    shuffle(rotor)
    print('Rotor aleatorio : {}'.format(rotor))    

def reflectorAleatorio(abecedario = ENGLISHDIC):
    abecedario = abecedario
    reflector = []
    num = [n for n in range(len(abecedario))]
    #Generamos el reflector desordenado
    while len(num) > 1:
        n = randint(1,len(num)-1)
        reflector.append((num[0],num[n]))
        reflector.append((num[n],num[0]))
        num.pop(n)
        num.pop(0)
    if len(num) == 1:
        reflector.append((num[0],num[0]))
    # Ordenamos el reflector
    reflector = sorted(reflector)
    print('Reflector aleatorio : {}'.format(reflector))  

if __name__ == '__main__':
    
    rotorAleatorio()
    reflectorAleatorio()
    

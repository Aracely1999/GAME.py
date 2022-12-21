import random
import os
MAX_FALLOS = 5
estaciones_del_año=[
    'Verano',
    'Invierno',
    'Primavera',
    'Otoño',
]
def crear_cadenas():
    estacion=random.choice(estaciones_del_año)
    espacio = '_' * len(estacion)
    return estacion, espacio
def reemplazar_simbolo(original,espacio, simbolo):
    cantidad= original.count(simbolo)
    inicio=0
    for i in range(cantidad):
        pos = original.find(simbolo, inicio)
        espacio= espacio[:pos] + simbolo + espacio[pos+1:]
        inicio= pos+1
    return espacio  
def ahorcado():
    print(f'hola vamos a jugar el juego del ahorcado,\
    La palabra oculta sera una estacion del año{len(estaciones_del_año)} intenta adivinar, \
    tienes hasta {MAX_FALLOS} intentos comencemos..')
    input('presiona enter para comenzar...')
    original, espacio= crear_cadenas()
    fallos=0
    while espacio != original and fallos < MAX_FALLOS:
        os.system('cls')
        print(f'palabra:{espacio}')
        s = input('¿cual simbolo quieres destapar?')
        if s in original:
            espacio=reemplazar_simbolo(original, espacio, s)
            print('Bien hecho! el simbolo es parte de la palabra')
        else:
            print('lo siento el simbolo no es parte de la palabra')
            fallos += 1
        input('Presiona enter para continuar...')
        os.system('cls')
    if espacio == original:
        print(f'felicidades la estacion es {espacio}')
    else:
        print(f' lo siento la estacion es:{original}') 
        print('Nos vemos....')
        os.system('cls')
def main():
    ahorcado()
if __name__=='__main__':
    main()
    #ESTE PROYECTO NO TIENE DERECHOS RESERVADOS
from os import system
import random

system('cls')
print("======================================================================")
print("            Bienvenido al Juego de adivinar un número    ")
print("======================================================================")

nombre=input('Ingresa tu nombre:')
print(f'\n\t{nombre}: Debes ingresar un número entre 1 y 100, para intentar adivinar el que')
print('\tha seleccionado la computadora. Tienes solo 8 intentos para descubrirlo')
n=0
bandera=False
numero=random.randint(1, 100)

while n<8:
    print (8-n)
    opcion=input('Ingresa un número del 1 al 100: ')

    if int(opcion)>1 and int(opcion)<100 and opcion.isdigit():
        n-=1
        if int(opcion)<numero:
            print('Sigue intentando.  El número ingresado es menor al que debes descubrir.')

        elif int(opcion)>numero:
            print('Sigue intentando.  El número ingresado es mayor al que debes descubrir.')

        else:
            print("FELICITACIONES!!! Has descubierto el número")
            bandera=True
            break

    else:
        print('Debes ingresar un número entero entre 1 y 100.-')
        input('<<ENTER>>')

if bandera:
    print(f"Lo descubriste en el intento: {8-n}")
    print("======================================================================")
    print("            Fin del Juego - Tu ganas    ")
    print("======================================================================")
else:
    print("======================================================================")
    print("            Fin del Juego - Has perdido la partida    ")
    print("======================================================================")
from os import system
import random

def encabezado(): # defino una función para el encabezado del juego
    system('cls')
    print("================ A D I V I N A    E L    N Ú M E R O ================\n")
    
encabezado()
nombre=input("Ingrese su nombre: ")
print(f"\n\t{nombre}: En este juego deberás adivinar el número aleatorio creado por la")
print("\tcomputadora, entre 1 y 100, para lo que podrás hacer tan solo ")
print("\tocho intentos, luego de los cuales habrás perdido el juego.")

input('<<ENTER>>')
intento=0  #inicio la variable de intentos en cero
valor_generado=random.randint(1,100)
control=False

while intento<8: 
    encabezado()
    print(f'-Le quedan {8-intento} intentos para ganar.-')
    numero=input('\n\tIngresa un número entre 1 y 100: ')
    
    if numero.isdigit() and int(numero)>=1 and int(numero)<=100: # Hago la validación del valor ingresado
        intento+=1 # sumo un intento solo si el valor ingresado es válido
        valor_elegido=int(numero)
        
        if valor_elegido<valor_generado:
            print('Haga un nuevo intento. El número ingresado es inferior.')
            input('<<ENTER>>')
                
        elif valor_elegido>valor_generado:
            print('Haga un nuevo intento. El número ingresado es superior.')
            input('<<ENTER>>')
            
        else:
            encabezado()
            control=True
            print(f"FELICITACIONES!!  Has ADIVINADO. El número es {valor_generado}!!")
            print(f"\tLo has logrado en {intento} intentos.")
            break

    else: # Lanza un mensaje cuando hubo una validación negativa del dato ingresado
        print('Debe ingresar un valor entero para juagar')

# ========================   una vez salido del WHILE, sigue por esta rutina

if control: # Aquí verifica si adivinó el número y finaliza el juego
    print("\n================= J U E G O    T E R M I N A D O ====================")
    
else:# Aquí verifica si no ha adivinado el número, notifica que ha perdido y finaliza
    encabezado()
    print(f"HAS PERDIDO EL JUEGO. El número que debías adivinar es el {valor_generado}.")
    print("\n================= J U E G O    T E R M I N A D O ====================")
    
    
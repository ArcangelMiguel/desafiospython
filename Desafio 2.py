'''crear un programa que le pida al usuario que ingresar un texto
cualquiera, por ejemplo, un artículo o una frase.
Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
elección.'''

text=input("Ingrese un texto cualquiera: ")
letra1=input("Ingrese la primera de tres letras: ").lower()
letra2=input("Ingrese la segunda de tres letras: ").lower()
letra3=input("Ingrese la tercera de tres letras: ").lower()

'''1- Cantidad de veces que aparece cada una de letras que eligió.'''
texto=text.lower()
print(f'\n\nLa letra {letra1} aparece {texto.count(letra1)} veces en el texto')
print(f'La letra {letra2} aparece {texto.count(letra2)} veces en el texto')
print(f'La letra {letra3} aparece {texto.count(letra3)} veces en el texto\n')

'''2- Cuantas palabras hay en total en todo el texto.'''

listaPalabras=text.split() # transforma el texto en una lista de palabras
print(f'El texto tiene un total de {len(listaPalabras)} palabras\n') # cuenta la cantidad de palabras

'''3- Cual es la primera letra y cuál es la última. (Indexación)'''

print(f'La primer letra del texto es: {text[0]}') # imprime la primer letra del texto
print(f'La ultima letra del texto es: {text[len(text)-1]}') # imprime la ultima letra del texto

'''4- Mostrar el texto en orden inverso.'''

print(f'\nEl texto en reversa es: {text[::-1]}') #muestra el texto en forma invertida

'''5- Decir si la palabra "python" aparece en el texto.'''

if 'python'in texto: # verifica la existencia de una palabra dentro del texto
    print('\nLa palabra Python aparece en el texto.')
else:
    print('\n\nLa palabra Python NO aparece en el texto.')
    
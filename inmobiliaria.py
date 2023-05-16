from os import system
from datetime import datetime

lista_inmueble=[{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

def sector(anio,sup,habit,garaje,sector):
    fecha_actual= datetime.now()
    anio_hoy=fecha_actual
    parcial=(sup*100+habit*500+garaje*1500)*(1-(2023-anio)/100)
    if sector.lower()=="a":
        precio=parcial
        return precio
    elif sector.lower()=="b":
        precio=parcial*1.5
        return precio
    elif sector.lower()=='c':
        precio=parcial*2
        return precio
    else:
        return 1


list_buscar=[]

system('cls')

print('==================================================================')
print('                       Gestión Inmobiliaria')
print('==================================================================')

print('\n\t Menu general')
print('1. Ingresar nueva propiedad.')
print('2. Modificar Estado de la Propiedad.')
print('3. Eliminar una Propiedad.')
print('4. Buscar por Monto.')
print('5. Salir de la Aplicación.\n')
opcion=input("Ingrese su opción: ")

if opcion=="1":
    anio=int(input('Año de la Propiedad: '))
    sup=int(input('Metros cuadrados: '))
    habit=int(input('Cant. Habitaciones: '))
    garaje=input('Garaje Si/No : ')
    zona=input('Elija la zona (A, B, C): ')
    estado=input('Seleccione estado (Disponible, Reservado, Vendido): ')





print(sector(2019,120,3,1,'a')        )


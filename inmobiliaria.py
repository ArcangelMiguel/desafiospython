from datetime import datetime



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

print(sector(2019,120,3,1,'a')        )


from os import system
#Declaro una lista vacía donde voy a almacenar los productos
pack=[]
ventas=[] #Declaro una lista de diccionarios con todas las ventas
venta=0 # Declaro una variable que almacene el total de la venta
        
#bucle para ejecutar todas las operaciones

while True:
    system('cls')
    print('Sistema de Ventas')
    print('  1- Ingresar un producto')
    print('  2- Vender')
    print('  3- Salir\n')
    opcion=int(input('Ingrese su opción: '))

    # analisis de la opción ingresada
    if opcion==1:
        # ingreso los datos de un producto y lo almaceno en un diccionario
        nombre=input('\n\tNombre del producto: ')
        descripcion=input('\tDetalle del producto: ')
        precio=int(input('\tPrecio: '))
        stock=int(input('\tStock: '))
        producto={'nombre':nombre, 'precio':precio, 'descr':descripcion,'cantidad':stock}
        pack.append(producto) #almaceno el diccionario en la lista
        
    elif opcion==2:
        # Muestro los productos disponibles para vender
        system('cls')
        print('Productos disponibles:')
        for s in pack:
            print(f"\t- {s['nombre']} \t cantidad: {s['cantidad']} unidades")
            
       
        opVenta=input('\nIngrese nombre del producto: ').lower()
        cantVenta=int(input('Ingrese cantidad a vender: '))
        estado=False #Defino una bandera en FALSE para controlar la existencia del producto
        for p in pack:
            if p['nombre'].lower()==opVenta:
                estado=True # Si se encuentra el producto a vender, la bandera cambia a TRUE
                if p['cantidad']>=cantVenta:
                    venta=cantVenta*p['precio']
                    diccVentas={'prod':p['descr'],'canVend':cantVenta,'montoVenta':venta} 
                    ventas.append(diccVentas)
                    print(f"La venta quedó registrada: {cantVenta} unidades de {p['nombre']}.-")
                    p['cantidad']-=cantVenta
                    break
                else:
                    print('No hay el stock que requiere')
                    input('Presione una tecla para seguir!')
                    break
        if estado==False:
            print("Este producto no existe.-")
            input('Presione una tecla para seguir!')
           
    elif opcion==3:
        system('cls')
        for p in ventas:
            print(f"Se vendió {p['prod']}: {p['canVend']} unidades, por $ {p['montoVenta']}")
        print('\nQueda el siguiente stock disponible:\n')
        
        for p in pack:
            print(f"\t {p['cantidad']} unidades de {p['descr']}.-")
        break
                 
       

import csv, os, time
from variables import *
bus = [["o" for x in range(1,5)] for y in range(7)]
Pasajeros = []
tarifa = 7000


while True:
    os.system('cls')
    print('\n\tBUSPE')
    print('''
    1.	Mostrar asientos disponibles
    2.  Comprar asiento
    3.	Mostrar ventas realizadas
    4.	Generar archivo CSV de ventas
    5.  Salir''')
    while True:
        try:
            opc = int(input("Ingrese una opcion: "))
            if opc in (1,2,3,4,5):
                break
            else:
                print('Ingrese una opcion correcta')
        except:
            print('ERROR, debe ser un numero entero')
    if opc==1:
        for f in bus:
            print (f)
    elif opc==2:

        print ("----ASIENTOS----")
        while True:
            nombre = input('Ingrese su nombre: ')
            if len(nombre) >= 3 and nombre.isalpha():
                break
            else:
                print('ERROR, DEBE TENER MAS DE 3 CARACTERES')
        while True:
                try:
                    edad = int(input('Ingrese su edad'))
                    if edad >= 0 and edad <= 110:
                        break
                    else:
                        print ('Debe ser entre 0 y 110')
                except:
                    print('ERROR, debe ingresar un numero entero')
        while True:
            try:
                telefono = int(input('Ingrese numero de telefono'))
                if (len(str(telefono))) == 9:
                    break
                else:
                    print('Debe tener 9 numeros')
            except:
                print ('ERROR, debe ser un numero entero')
        while True:
            try:
                fila = int(input('Ingrese la fila: '))
                columna = int(input('Ingrese la columna: '))
                if bus[fila-1][columna-1]=="o":
                     bus[fila-1][columna-1] = "x"
                     print('Asiento elegido correctamente')
                     break
                else:
                     ('El asiento esta ocupado')
            except:
                 print('ERROR, debe ser un numero entero')

        print ('Su edad es',edad)
        if edad <= 18
        
        Pasajeros = {
            "NOMBRE":nombre,
            "EDAD":edad,
            "TELEFONO":edad,
            "FILA":fila,
            'COLUMNA':columna
        }
        
        
    elif opc==3:
        if not Pasajeros:
            break
        else:
            for x in Pasajeros:
                print(f"Nombre",{x["NOMBRE"]})
                print(f"Edad",{x["EDAD"]})
                print(f"Telefono",{x["TELEFONO"]})
                print(f"Fila",{x["FILA"]})
                print(f"Columna",{x["COLUMNA"]})
    elif opc==4:
        pass
    else:
        print ('GRACIAS POR SU COMPRA ADIOS')
        pass
    time.sleep(3)
        



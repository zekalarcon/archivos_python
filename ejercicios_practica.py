#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Ezequiel Alarcon"
__email__ = "zekalarcon@gmail.com"


import csv
import re


def ej1():
    # Ejercicios con archivos txt

    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea a linea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leaidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''

    contar_lineas = 0

    with open('texto.txt', 'r') as fi:
        for lineas in fi:
            contar_lineas += 1

    print(f'La cantidad de lineas en el archivo texto.txt son: {contar_lineas}')


def ej2():
    # Ejercicios con archivos txt
    
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura (write)

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''

    # fi = open('nota.txt', 'r')
    # fo = open(.......)

    # Recuerde cerrar los archivos al final ;)

    cantidad_lineas = 0
    fi = open('notas.txt', 'r')
    fo = open('notas_copiadas.txt', 'w')

    for lineas in fi:
        fo.writelines(lineas)
        cantidad_lineas += 1

    fi.close()
    fo.close() 

    print(f'La cantidad de lineas copiadas fueron: {cantidad_lineas}')   
            


def ej3():
    # Ejercicios con archivos CSV
    
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrar dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''


    dos_ambientes = 0
    tres_ambientes = 0
    
    
    with open('propiedades.csv', 'r') as fi:
        reader = list(csv.DictReader(fi))
        len_reader = len(reader)

    
    with open('propiedades_dos_amb.csv', 'w', newline='') as fo:
        header = ['','fecha','latitud','longitud','url','titulo','tipo_propiedad','precio','moneda','m2','ambientes']
        propiedades_dos_amb = csv.DictWriter(fo, fieldnames=header)
        propiedades_dos_amb.writeheader()


        for i in range(len_reader):
            row = reader[i]
            ambientes = str(row.get('ambientes'))
            if ambientes == '2': 
                propiedades_dos_amb.writerow(row)   
                dos_ambientes +=1


    with open('propiedades_tres_amb.csv', 'w', newline='') as fo:
        header = ['','fecha','latitud','longitud','url','titulo','tipo_propiedad','precio','moneda','m2','ambientes']
        propiedades_tres_amb = csv.DictWriter(fo, fieldnames=header)
        propiedades_tres_amb.writeheader()    

        
        for i in range(len_reader):
            row = reader[i]
            ambientes = str(row.get('ambientes'))
            if ambientes == '3':
                propiedades_tres_amb.writerow(row)
                tres_ambientes += 1

    
    print(f'Las {dos_ambientes} propiedades de 2 ambientes fueron guardadas en el archivo "propiedades_dos_amb.csv" ')
    print(f'Las {tres_ambientes} propiedades de 3 ambientes fueron guardadas en el archivo "propiedades_tres_amb.csv" ')

        
    
   

def ej4():
    # Ejercicios con diccionarios
    

    '''
    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario "inventario" el par:
    <fruta>:<cantidad>
    El diccionario "inventario" ya viene cargado
    con el valor el stock de manzanas para que vean
    de ejemplo.
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"

    '''

    # En el bucle realizar:
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"

    
    inventario = {'manzanas': 6}

    
    print('Ingreso de frutas/verduras y su cantidad para realizar stock')    

    
    while True:    
        agregar_item = input('Ingrese fruta/verdura o "FIN" para terminar:\n')
        if agregar_item == 'FIN':
            break
        cantidad = int(input('Ingrese cantidad:\n'))
        inventario[agregar_item] = cantidad
    
    
    print(f'Se actualizo su inventario: {inventario}')    
        


def ej5():
    # Ejercicios con archivos CSV
    

    '''
    Parecido al el ejercicio anterior, genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'

    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario, que utilizaremos para escribir en el archivo CSV:

    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    Ojo! No es igual al diccionario del anterior ejercicio, 
    porque el anterior usaba como "clave" el nombre de la fruta.
    Ahora tenemos dos pares de valores "clave: valor", pueden
    ver el inventario con el ejemplo de la manzana.

    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"

    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''
    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.

    # Bucle....

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})


    with open('frutas_verduras_stock.csv', 'w', newline='') as fo:
        header = ['Fruta/Verdura', 'Cantidad']
        frutas_verduras_stock = csv.DictWriter(fo, fieldnames=header)
        frutas_verduras_stock.writeheader()

        
        while True:
            fruta_verdura = input('Ingrese fruta/verdura:\n')
            if fruta_verdura == 'FIN':
                break
            cantidad = int(input('Ingrese cantida:\n'))
            frutas_verduras_stock.writerow({'Fruta/Verdura':fruta_verdura, 'Cantidad':cantidad})

    
    print('Archivo "frutas_verduras_stock.csv" creado y actualizado con stock')



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    ej3()
    #ej4()
    #ej5()

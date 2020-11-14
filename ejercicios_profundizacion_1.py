#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Ezequiel Alarcon"
__email__ = "zekalarcon@gmail.com"


import csv

def ej1():
    print("Cuenta caracteres")
    cantidad_letras = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "texto.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''


    with open('texto.txt', 'r') as fi:
        for line in fi:
            cantidad_letras += len(line)
        print(f'La cantidad de caracteres en el archivo "texto.txt" son: {cantidad_letras}')    



def ej2():
    print("Transcribir!")
    
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''
    

    cantidad_letras = 0

    
    with open('texto_contado.txt', 'w') as fo:
        while True:
            texto = input('Ingrese texto:\n')
            if texto == '':
                break
            fo.writelines(texto + '\n')
            cantidad_letras += len(texto) + 1 
        
    
    print(f'La cantidad de caracteres en el texto son: {cantidad_letras}')      


def ej3():
    print("Escrutinio de los alquileres de Capital Federal")
    

    '''
    Realizar un prorgrama que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''
    contador = 0
    suma_precio = 0
    

    with open('propiedades.csv', 'r') as fi:
        reader = list(csv.DictReader(fi))
        len_reader = len(reader)
    

        while True:
            minimo = None
            maximo = None
            cantidad_ambientes = input('Ingrese cantidad de ambientes o "FIN" para terminar:\n')
            if cantidad_ambientes == 'FIN':
                break
            for i in range(len_reader):
                row = reader[i]
                ambientes = row.get('ambientes')
                moneda = row.get('moneda')
                precio = row.get('precio')
                if ambientes == cantidad_ambientes and moneda == 'ARS':
                    contador += 1
                    suma_precio += float(precio)
                    if maximo == None or maximo < float(precio):
                        maximo = float(precio)
                    if minimo is None or float(precio) < minimo:
                        minimo = 0
                        minimo = float(precio)
            
            
            print(f'La cantidad de departamentos en alquiler de {cantidad_ambientes} ambientes es: {contador}')
            print(f'El promedio de los alquileres de departamentos en pesos, es: ${suma_precio/contador:.2f}')
            print(f'El departamento mas caro es: {maximo}')   
            print(f'EL departamento mas barato es: {minimo}') 




if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()

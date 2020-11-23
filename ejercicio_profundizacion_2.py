#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Ezequiel Alarcon"
__email__ = "zekalarcon@gamil.com"



import csv
from datetime import datetime, time
from time import gmtime, strftime


def ironman():
    print("Ahora sí! buena suerte :)")

    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    NOTA IMPORTANTE:
    En este ejercicio se pide calcular el promedio, el máximo y mínimo tiempo
    que realizaron los corredores en distintas etapas de la carrera.
    La dificultad radica en que el dato que el archivo nos provee está
    en el siguiente formado:

    hora:minutos:segundos, 0:47:27 --> (0 horas, 47 minutos, 27 segundos).

    No pueden utilizar este valor para calcular el promedio, el máximo
    y mínimo ya que está en formato texto, no está en formato numérico.
    Para poder realizar cálculos matemáticos sobre este dato deben primero
    llevarlo a un formato que les permita realizar cálculos.

    Normalmente en estos casos lo que se realiza es llevar este dato
    0:47:27 a segundos, es decir, calcular cuantos segundos le llevó
    al corredor completar esa etapa, ya que segundos es la unidad mínima
    presentada (horas, minutos, segundos).

    Para poder calcular la cantidad de segundos totales deberían operar
    de la siguiente forma:

    segundos_totales = horas * 3600 + minutos * 60 + segundos

    De esta forma están pasando de un formato texto horas:minutos:segundos a
    un número "segundos_totales" el cual pueden calcular
    promedio, máximo y mínimo
    
    Queda en sus manos pensar como extraer las "horas" "minutos" y "segundos"
    del formato "horas:minutos:segundos", 
    pueden realizar operaciones de texto ahí, o usar algún módulo externo
    de Python que resuelva este problema.

    '''
    contador_segundos = 0
    nadar = []
    bici = []
    correr = []
    
    
    
    with open('2019 Ironman World Championship Results.csv', 'r') as fi:
        reader = list(csv.DictReader(fi))
        len_reader = len(reader)
    
        
        while True:
            opcion = input('Ingrese categoria para ver resultados o "FIN" para terminar:\n')
            if opcion == 'FIN':
                break
            for i in range(len_reader):
                row = reader[i]
                division = row.get('Division')
                swim = row.get('Swim')
                bike = row.get('Bike')
                run = row.get('Run')
                if opcion == division:
                    nadar.append(swim)
                    bici.append(bike)
                    correr.append(run)
            

            for i in nadar:
                while '' in nadar:
                    nadar.remove('')
                seconds = segundos(i)
                contador_segundos += seconds
                promedio = contador_segundos / len(nadar)
                promedio_nadar = prom(promedio)

        
            for i in bici:
                while '' in bici:
                    bici.remove('')
                seconds = segundos(i)
                contador_segundos += seconds
                promedio = contador_segundos / len(bici)
                promedio_bici = prom(promedio)


            for i in correr:
                while '' in correr:
                    correr.remove('')
                seconds = segundos(i)
                contador_segundos += seconds
                promedio = contador_segundos / len(correr)
                promedio_correr = prom(promedio)


            print(f'El promedio en la categoria {opcion} disciplina Swim es: {promedio_nadar}')     
            print(f'El maximo tiempo en la categoria {opcion} disciplina Swim es: {max(nadar)}')
            print(f'El minimo tiempo en la categoria {opcion} disciplina Swim es: {min(nadar)}\n')

            print(f'El promedio en la categoria {opcion} disciplina Bike es: {promedio_bici}')     
            print(f'El maximo tiempo en la categoria {opcion} disciplina Bike es: {max(bici)}')
            print(f'El minimo tiempo en la categoria {opcion} disciplina Bike es: {min(bici)}\n')

            print(f'El promedio en la categoria {opcion} disciplina Run es: {promedio_correr}')     
            print(f'El maximo tiempo en la categoria {opcion} disciplina Run es: {max(correr)}')
            print(f'El minimo tiempo en la categoria {opcion} disciplina Run es: {min(correr)}\n')
    

def segundos(i):
    seconds = 0
    formato = "%H:%M:%S"
    h = datetime.strptime(i,formato)
    seconds = h.hour * 3600 + h.minute * 60 + h.second
    return seconds  


def prom(promedio):   
    promedios = strftime("%H:%M:%S", gmtime(promedio))
    return promedios



if __name__ == '__main__':
    print("Ejercicios de práctica extra")
    ironman()

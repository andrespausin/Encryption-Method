# Programa de Encriptación
# Elaborado por: César Pausín 28.402.367
#                Santiago Briceño 28.063.634
# Seguridad en Redes

# Programa que encripta y desencripta el valor de una cadena. Consiste en poder encriptarlo dependiendo de la hora a la que es ejecutado el programa, evaluado en 
# si es primo o no.

import datetime
import random

# Función que nos permite determinar la hora a la que es ejecutado un programa
def det_hora():
    hora = datetime.datetime.now().hour
    return hora

# Función que nos permite determinar si la hora a la que es ejecutada el programa es primo o no
def is_primo(number):
    result = True
    i = 2
    # Si el número es mayor a 2, se determina si es primo o no
    if (number > 2):
        # Se tiene un contador que aumenta en caso de que el número sea divisible por otro número más que el 1 y el mismo
        while (result and i < number):
            result = number % i != 0
            i += 1
    return result

# Función que encripta un mensaje
def encrypt(cadena, characters, characters2, hour):
    # print(str(hour.hour) + '\n')
    key = is_primo(hour)
    cadena = cadena.upper()
    data = ''

    # En caso de que el valor de la hora sea primo, se sañadirán 3 carácteres entre caracteres de cadena de entrada
    if (key):

        for i in range(len(cadena)):
            # Si la cadena tiene un espacio, elige los valores de la lista auxiliar
            if (cadena[i].isspace()):
                data += characters2[random.randint(0, len(characters2)-1)] + characters2[random.randint(0, len(characters2)-1)] + characters2[random.randint(0, len(characters2)-1)]

            # Caso contrario, elige los valores de la lista principal
            else:
                data += characters[random.randint(0, len(characters)-1)] + characters[random.randint(0, len(characters)-1)] + characters[random.randint(0, len(characters)-1)] + cadena[i]

        data += characters[random.randint(0, len(characters)-1)] + characters[random.randint(0, len(characters)-1)] + characters[random.randint(0, len(characters)-1)]

    # En caso de que el valor de la hora no sea primo, se añadirá un carácter entre cadena de caracteres de la cadena de entrada
    else:
        for i in range(len(cadena)):

            # Si la cadena tiene un espacio, elige los valores de la lista auxiliar
            if (cadena[i].isspace()):
                data += characters2[random.randint(0, len(characters2)-1)]

            # Caso contrario, elige los valores de la lista principal
            else:
                data += characters[random.randint(0, len(characters)-1)] + cadena[i]

        data += characters[random.randint(0, len(characters)-1)]

    # Retorna un diccionario que contiene información de un booleano que nos indica si la hora a la que se ejecutó es primo o no, 
    result = {
        'key': key,
        'data': data
    }
    return result

# Method that desencrypt
def decrypt(result, characters, characters2, hour):
    key = result['key']
    old_data = result['data']
    data = ''
    i = 0
    # Si la hora es un número primo
    if (key):

        while(i < len(old_data)):
        # for i in range(len(old_data)):
            # Si el valor de la cadena actual está en el array de espacios
            if (old_data[i] in characters2):
                # Si los dos valores siguientes son del segundo array de valores es un espacio
                if (old_data[i+1] in characters2 and old_data[i+2] in characters2):
                    data += ' '
                    i+= 3
                # Caso contrario, no agrega nada a data y aumenta el valor del índice
                else:
                    data += ''
                    i+=1
            # En caso de que esté en el primer array de valores
            else:
                # Si el índice está antes de los últimos 3 valores del array, elige los valores cada 3 letras
                if (i < len(old_data)-3):
                    data += old_data[i+3]
                    i+=4
                # Caso contrario, no agrega nada a data y aumenta en 1 el valor del índice
                else:
                    data += ''
                    i+=1
    # Si la hora es un número no primo
    else:
        while(i < len(old_data)):
        # for i in range(len(old_data)):
            # Si el valor de la cadena actual está en el array de espacios
            if (old_data[i] in characters2):
                # Si los dos valores siguientes es un valor dentro del primer array
                if (old_data[i+1] in characters):
                    data += ' '
                    i+= 1
                # Caso contrario, no agrega valor a data y aumenta el contador
                else:
                    data += ''
                    i+=1
            # En caso de que esté en el primer array de valores
            else:
                # Si el índice está antes de los últimos 3 valores del array, elige los valores cada letra de diferencia
                if (i < len(old_data)-1):
                    data += old_data[i+1]
                    i+=2
                else:
                    # Caso contrario, no agrega nada a data y aumenta en 1 el valor del índice
                    data += ''
                    i+=1
    # Retorna una cadena con la desencriptación del mensaje
    return data


# Programa principal

# Declaración de Variables

# Variables de Entrada
str_entrada = str
resultdo = {}
cent = str

#Variables de Salida
str_salida = str

# Variables del proceso
hour =  int
#Arreglos que nos permite determinar si un caracter encriptado es o no un espacio
characters = 'ABCDEFGHIJKLMNOPQRSTU12345'
characters2 = 'VWXYZ67890'

cent = 's'

while cent == 's' or cent =='S':

    print('\nInicio del Programa\n')

    # Lectura de Datos
    str_cadena = input('Indique el mensaje que desea encriptar: ')

    print('\nMensaje: {}\n'.format(str_cadena.upper()))

    # Procesamiento de variables
    hour = det_hora()

    #Procesamiento de Datos
    resultado = encrypt(str_cadena, characters, characters2, hour)

    print('\nEncriptación: {}\n'.format(resultado['data']))

    str_salida = decrypt(resultado, characters, characters2, hour)

    print('\nDesencriptado: {}\n'.format(str_salida))

    cent = input('\n¿Desea volver a probar el programa? (S/N): ')






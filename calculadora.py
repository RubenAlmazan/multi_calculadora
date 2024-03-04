import os
from math import sqrt
import math

# CALCULADORA

# Funcion de Suma
def suma():
    
    # Validacion de numeros, si no, devuelve error - None
    try:
        uno = int(input('Ingrese un número: '))
        dos = int(input('Ingrese otro número: '))
    except ValueError:
        return print('\nIngrese numeros validos, intentelo de nuevo')

    # Se realiza operacion y se devuelve resultado en return
    result = uno + dos
    return result

# Funcion de resta
def resta():
    
    # Validacion de numeros, si no, devuelve error - None
    try:
        uno = int(input('Ingrese un número: '))
        dos = int(input('Ingrese otro número: '))
    except ValueError:
        return print('\nIngrese numeros validos, intentelo de nuevo')

    # Se realiza operacion y se devuelve resultado en return
    result = uno - dos
    return result

# Funcion de multiplicacion
def multi():
    
    # Validacion de numeros, si no, devuelve error - None
    try:
        uno = int(input('Ingrese un número: '))
        dos = int(input('Ingrese otro número: '))
    except ValueError:
        return print('\nIngrese numeros validos, intentelo de nuevo')

    # Se realiza operacion y se devuelve resultado en return
    result = uno * dos
    return result

# Funcion de division
def divi():
    
    # Validacion de numeros, si no, devuelve error - None
    try:
        uno = int(input('Ingrese un número: '))
        dos = int(input('Ingrese otro número: '))
    except ValueError:
        return print('\nIngrese numeros validos, intentelo de nuevo')

    # Se realiza operacion y se devuelve resultado en return
    result = uno / dos
    return result

# Funcion de porcentaje
def porcentaje():
    
    # Validacion de numeros, si no, devuelve error - None
    try:
        uno = int(input('Ingrese un número: '))
        dos = int(input('Ingrese otro número: '))
    except ValueError:
        return print('\nIngrese numeros validos, intentelo de nuevo')

    # Se realiza operacion y se devuelve resultado en return
    result = uno * (dos/100)
    return result

# Funcion de raiz cuadrada
def raiz_cuadrada():
    
    # Validacion de numeros, si no, devuelve error - None
    try:
        uno = int(input('Ingrese un número: '))
    except ValueError:
        return print('\nIngrese numeros validos, intentelo de nuevo')

    # Se realiza operacion y se devuelve resultado en return
    result = sqrt(uno)
    return result

# Funcion de seno
def seno():
    
    # Validacion de numeros, si no, devuelve error - None
    try:
        uno = int(input('Ingrese un número de grados: '))
    except ValueError:
        return print('\nIngrese numeros validos, intentelo de nuevo')

    # Se realiza operacion y se devuelve resultado en return
    result = math.sin(uno)
    return result

#Funcion de coseno
def coseno():
    
    # Validacion de numeros, si no, devuelve error - None
    try:
        uno = int(input('Ingrese un número de grados: '))
    except ValueError:
        return print('\nIngrese numeros validos, intentelo de nuevo')

    # Se realiza operacion y se devuelve resultado en return
    result = math.cos(uno)
    return result

# Funcion de tangente
def tangente():
    
    # Validacion de numeros, si no, devuelve error - None
    try:
        uno = int(input('Ingrese un número de grados: '))
    except ValueError:
        return print('\nIngrese numeros validos, intentelo de nuevo')

    # Se realiza operacion y se devuelve resultado en return
    result = math.tan(uno)
    return result

# Funcion del factorial
def factorial():
    
    # Validacion de numeros, si no, devuelve error - None
    try:
        uno = int(input('Ingrese un número: '))
    except ValueError:
        return print('\nIngrese numeros validos, intentelo de nuevo')
    
    # Se realiza operacion y se devuelve resultado en return
    a = 1; total = 1
    
    while a <= uno:
        total = total * a
        a += 1
    
    result = total
    return result

# Funcion de numero al cuadrado
def cuadrado():
    
    # Validacion de numeros, si no, devuelve error - None
    try:
        uno = int(input('Ingrese un número: '))
    except ValueError:
        return print('\nIngrese numeros validos, intentelo de nuevo')

    # Se realiza operacion y se devuelve resultado en return
    result = uno * uno
    return result

# Funcion de numero elevado a la N potencia 
def potencia():
    
    # Validacion de numeros, si no, devuelve error - None
    try:
        uno = int(input('Ingrese un número: '))
        valor = int(input('Ingrese la potencia a la que elevará dicho numero: '))
    except ValueError:
        return print('\nIngrese numeros validos, intentelo de nuevo')

    # Se realiza operacion y se devuelve resultado en return
    result = pow(uno, valor)
    return result

# Funcion de decimal a binario
def dec_a_bin():
    
    # Validacion de numeros, si no, devuelve error - None
    try:
        uno = int(input('Ingrese un número: '))
    except ValueError:
        return print('\nIngrese numeros validos, intentelo de nuevo')

    # Se realiza operacion y se devuelve resultado en return
    divisor = uno
    lista=[]

    while divisor != 0:
        valor = divisor % 2
        divisor = divisor // 2  
        lista.append(valor)

    result = lista[::-1]
    result = ''.join(map(str, result))
    return result

# Funcion Binario a Decimal
def bin_a_dec():
    uno = str(input('Ingrese un número binario: '))
    
    numero = str(uno)
    lista = list(uno)
    
    # Validacion de numeros, si no, devuelve error - None
    for elemento in lista:
        if elemento != '0' and elemento != '1':
            return print('\nIngrese numeros validos, intentelo de nuevo')
        
    potencia = len(numero)

    # Se realiza operacion y se devuelve resultado en return
    a = 0; suma = 0
    while a < len(numero):
        suma = suma + (int(numero[a]) * pow(2, potencia-1))
        potencia = potencia -1
        a += 1

    result = suma
    return result

# Funcion Decimal a Octal
def dec_a_oct():
    
    # Validacion de numeros, si no, devuelve error - None
    try:
        uno = int(input('Ingrese un número: '))
    except ValueError:
        return print('\nIngrese numeros validos, intentelo de nuevo')
    
    divisor = uno
    lista=[]

    # Se realiza operacion y se devuelve resultado en return
    while divisor != 0:
        valor = divisor % 8
        divisor = divisor // 8  
        lista.append(valor)

    result = lista[::-1]
    result = ''.join(map(str, result))

    return result

# Funcion de octal a decimal
def oct_a_dec():
    uno = str(input('Ingrese un número octal: '))
    
    lista = list(uno)
    cifra = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    # Validacion de numeros, si no, devuelve error - None
    for elemento in lista:
        if elemento not in cifra:
            return print('\nIngrese numeros validos, intentelo de nuevo')
        
    numero = str(uno)
    potencia = len(numero)

    # Se realiza operacion y se devuelve resultado en return
    a = 0; suma = 0
    while a < len(numero):
        suma = suma + (int(numero[a]) * pow(8, potencia-1))
        potencia = potencia -1
        a += 1

    result = suma
    
    return result

# Funcion Decimal a hexadecimal
def dec_a_hex():
    
    # Validacion de numeros, si no, devuelve error - None
    try:
        uno = int(input('Ingrese un número: '))
    except ValueError:
        return print('\nIngrese numeros validos, intentelo de nuevo')
    
    divisor = uno
    hexa={10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    lista=[]

    # Se realiza operacion y se devuelve resultado en return
    while divisor != 0:
        valor = divisor % 16
        divisor = divisor // 16
        
        if valor in hexa:
            valor = hexa[valor]
            
        lista.append(valor)

    result = lista[::-1]
    result = ''.join(map(str, result))

    return result

# Funcion Hexadecimal a Decimal 
def hex_a_dec():
    uno = str(input('Ingrese un número: '))

    numero = str(uno)
    potencia = len(numero)
    hexa={'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    cifra = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    validar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F']

    # Validacion de numeros, si no, devuelve error - None
    for elemento in uno:
        if(elemento not in validar) :
            return print('\nIngrese numeros validos, intentelo de nuevo')
        
    # Se realiza operacion y se devuelve resultado en return
    a = 0; suma = 0
    while a < len(numero):
        potencia = potencia -1
        
        if(numero[a] in cifra):
            suma = suma + (int(numero[a]) * pow(16, potencia))
        else:
            suma = suma + (hexa[numero[a]] * pow(16, potencia))
        
        a += 1

    result = suma
    
    return result

#######################################################################################

# Menu Principal

puerta = True

while puerta == True:
    
    print("\n       ******************     PROYECTO 1 -- CALCULADORA     ******************      \n")
    print("  ------------------------------------------------------------------------------------")
    print("  1) SUMA            2) RESTA                 3) MULTIPLICACION        4) DIVISION")
    print("  5) PORCENTAJE      6) RAIZ CUADRADA ")
    print("  7) SENO            8) COSENO                9) TANGENTE              10) FACTORIAL")
    print("  11) NUMERO ELEVADO AL CUADRADO              12) NUMERO ELEVADO A LA N POTENCIA")
    print("  13) CONVERSION DE DECIMAL A BINARIO         14) CONVERSION DE BINARIO A DECIMAL")
    print("  15) CONVERSION DE DECIMAL A OCTAL           16) CONVERSION DE OCTAL A DECIMAL")
    print("  17) CONVERSION DE DECIMAL A HEXADECIMAL     18) CONVERSION DE HEXADECIMAL A DECIMAL")
    print("  ------------------------------------------------------------------------------------")
    print("  0) SALIR")

    # Validacion de opción a seleccionar, si hay error, excede el limite de 'a'
    # Se declara como 'Entrada no valida' y vuelve a preguntar opcion
    try:
        a = int(input('\nIngrese una opción válida: '))
    except ValueError:
        a = 20

    # Cierre del programa
    if(a == 0): 
        puerta = False
        
    # Opciones de calculadora
    # Al dar valor a la variante 'a', se accede a la funcion seleccionada
    elif(a == 1):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                        SUMA                        ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', suma(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
    
    elif(a == 2):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                       RESTA                        ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', resta(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
    
    elif(a == 3):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                  MULTIPLICACION                    ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', multi(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif(a == 4):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                     DIVISION                       ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', divi(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

    elif(a == 5):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                    PORCENTAJE                      ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', porcentaje(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
     
    elif(a == 6):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                   RAIZ CUADRADA                    ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', raiz_cuadrada(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
           
    elif(a == 7):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                        SENO                        ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', seno(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
    
    elif(a == 8):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                       COSENO                       ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', coseno(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
       
    elif(a == 9):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                      TANGENTE                      ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', tangente(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif(a == 10):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                     FACTORIAL                      ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', factorial(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif(a == 11):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                 ELEVADO AL CUADRADO                ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', cuadrado(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif(a == 12):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('               ELEVADO A LA N POTENCIA              ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', potencia(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif(a == 13):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                  DECIMAL A BINARIO                 ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', dec_a_bin(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif(a == 14):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                  BINARIO A DECIMAL                 ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', bin_a_dec(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif(a == 15):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                   DECIMAL A OCTAL                  ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', dec_a_oct(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
    
    elif(a == 16):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                    OCTAL A DECIMAL                 ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', oct_a_dec(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
          
    elif(a == 17):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                 DECIMAL A HEXADECIMAL              ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', dec_a_hex(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif(a == 18):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('                 HEXADECIMAL A DECIMAL              ')
        print('----------------------------------------------------')
        print('\nLa respuesta es:', hex_a_dec(), '\n')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    # Caso de error o caracteres no validos
    elif(a > 18):
        
        print('----------------------------------------------------')
        print('                   ENTRADA NO VALIDA                ')
        print('----------------------------------------------------')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    else:
        print('----------------------------------------------------')
        print('         OCURRIO UN ERROR, INTENTE DE NUEVO         ')
        print('----------------------------------------------------')
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')


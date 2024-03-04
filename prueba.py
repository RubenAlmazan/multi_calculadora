def hex_a_dec():
    uno = str('37C1Z')
    #uno = str(input('Ingrese un número: '))

    numero = str(uno)
    potencia = len(numero)
    hexa={'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    cifra = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    validar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F']

    for elemento in uno:
        if(elemento not in validar) :
            return print('\nIngrese numeros validos, intentelo de nuevo')
        
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

print(hex_a_dec())

"""def bin_a_dec():
    
    uno = str(110111)
    
    numero = str(uno)
    lista = list(uno)

    for elemento in lista:
        if elemento != '0' and elemento != '1':
            return False
    
    potencia = len(numero)

    a = 0; suma = 0
    while a < len(numero):
        suma = suma + (int(numero[a]) * pow(2, potencia-1))
        potencia = potencia -1
        a += 1

    result = suma
    return result

print(bin_a_dec())"""

"""numero = str('1A3')
potencia = len(numero)
hexa={'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
cifra = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

a = 0; suma = 0
while a < len(numero):
    #suma = suma + (int(numero[a]) * pow(16, potencia-1))
    potencia = potencia -1
    
    if(numero[a] in cifra):
        suma = suma + (int(numero[a]) * pow(16, potencia))
    else:
        suma = suma + (hexa[numero[a]] * pow(16, potencia))
    
    a += 1

print(suma)"""

"""
uno = 141 
divisor = uno
hexa={10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
lista=[]

while divisor != 0:
    valor = divisor % 16
    divisor = divisor // 16
    
    if valor in hexa:
        print(hexa[valor])
        valor = hexa[valor]
        
    lista.append(valor)

result = lista[::-1]
print(result)"""

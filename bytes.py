from pydes import *

import csv

# # CREACION DE NUMEROS 2^24
decimal = 0
file = open('combinaciones.csv', 'w')
while True:
    bin_str = str(bin(decimal))
    bin_str = bin_str[2:len(bin_str)]
    if len(bin_str) < 24:
        for x in range(0, 24 - len(bin_str)):
            bin_str = '0' + bin_str[0:]
        if bin_str[7] == '0' and bin_str[15] == '0' and bin_str[-1] == '0':
            bin_str = bin_str[0:8] + ',' + bin_str[8:16] + ',' + bin_str[16:]
            file.write('00000000,00000000,00000000,00000000,00000000,' + bin_str + '\n')
    elif len(bin_str) == 24:
        if bin_str[7] == '0' and bin_str[15] == '0' and bin_str[-1] == '0':
            bin_str = bin_str[0:8] + ',' + bin_str[8:16] + ',' + bin_str[16:]
            file.write('00000000,00000000,00000000,00000000,00000000,' + bin_str + '\n')
    elif len(bin_str) > 24:
        break
    decimal = decimal + 1
file.close()

# # conversion binaria a caracteres
entrada = open('combinaciones.csv', 'r')
reader = csv.reader(entrada, delimiter=',')
salida = open('claves.txt', 'w')
caracter = ''
for linea in reader:
    salida.write(str(str(int(str(linea[0]), 2)).encode('utf-8') + str(int(str(linea[1]), 2)).encode('utf-8')
                 + str(int(str(linea[2]), 2)).encode('utf-8') + str(int(str(linea[3]), 2)).encode('utf-8')
                 + str(int(str(linea[4]), 2)).encode('utf-8') + str(int(str(linea[5]), 2)).encode('utf-8')
                 + str(int(str(linea[6]), 2)).encode('utf-8') + str(int(str(linea[7]), 2)).encode('utf-8')))
    salida.write('\n')

entrada.close()
salida.close()


# CIFRADO DES
texto_plano = "8AB9CD0EF1AB2CDE"
texto_cifrado = "B3D3D9D988E4B78E"

d = des()

# CIFRADO DE TEXTO PLANO
entrada = open('archivoJ.txt', 'r')
salida = open('textos_cifrados.txt', 'w')

for clave in entrada:
    cyphered = d.encrypt(clave, texto_plano)
    salida.write(str(clave) + " " + str(cyphered.encode('utf-8'))+"\n")

entrada.close()
salida.close()

# DESCIFRADO DE TEXTO CIFRADO
entrada = open('archivoJ.txt', 'r')
salida = open('textos_descifrados.txt', 'w')

for clave in entrada:
    deciphered = d.decrypt(clave, texto_cifrado)
    salida.write(str(clave) + str(deciphered.encode('utf-8')) + "\n")

entrada.close()
salida.close()

# LIMPIAR EL ARCHIVO ELIMINANDO LOS \n INNECESARIOS
f_textos_cifrados = open('textos_cifrados.txt', 'r')
f_textos_cifrados_limpio = open('textos_cifrados_limpio.txt', 'w')
x = 1
limpio = ""

for linea in f_textos_cifrados:
    if x % 2 == 0:
        limpio += linea
        f_textos_cifrados_limpio.write(limpio)
        limpio = ""
    else:
        limpio = linea.replace("\n", "")
    x += 1

f_textos_cifrados.close()
f_textos_cifrados_limpio.close()

f_textos_descifrados = open('textos_descifrados.txt', 'r')
f_textos_descifrados_limpio = open('textos_descifrados_limpio.txt', 'w')
x = 1
limpio = ""

for linea in f_textos_descifrados:
    if x % 2 == 0:
        limpio += linea
        f_textos_descifrados_limpio.write(limpio)
        limpio = ""
    else:
        limpio = linea.replace("\n", "")
    x += 1

f_textos_descifrados.close()
f_textos_descifrados_limpio.close()


f_cifrados = open('textos_cifrados_limpio.txt', 'r')
f_descifrados = open('textos_descifrados_limpio.txt', 'r')
bandera = 0
aux1 = ""
aux2 = ""

for f1 in f_cifrados:
    aux1 = f1.split(" ")
    for f2 in f_descifrados:
        aux2 = f2.split(" ")
        if aux1[1] == aux2[1]:
            print("Claves encontradas"
                  + "clave 1: " + aux1[0] + "\n"
                  + "clave 2: " + aux1[0])
            bandera = 1
            break
    if bandera == 1:
        break

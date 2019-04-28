from pydes import *
import csv

# CREACION DE NUMEROS 2^24
# decimal = 0
# file = open('combinaciones.csv', 'w')
# while True:
#     bin_str = str(bin(decimal))
#     bin_str = bin_str[2:len(bin_str)]
#     if len(bin_str) < 24:
#         for x in range(0, 24 - len(bin_str)):
#             bin_str = '0' + bin_str[0:]
#         if bin_str[7] == '0' and bin_str[15] == '0' and bin_str[-1] == '0':
#             bin_str = bin_str[0:8] + ',' + bin_str[8:16] + ',' + bin_str[16:]
#             file.write('00000000,00000000,00000000,00000000,00000000,' + bin_str + '\n')
#     elif len(bin_str) == 24:
#         if bin_str[7] == '0' and bin_str[15] == '0' and bin_str[-1] == '0':
#             bin_str = bin_str[0:8] + ',' + bin_str[8:16] + ',' + bin_str[16:]
#             file.write('00000000,00000000,00000000,00000000,00000000,' + bin_str + '\n')
#     elif len(bin_str) > 24:
#         break
#     decimal = decimal + 1
# file.close()

# conversion binaria a caracteres
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

# # CIFRADO DES
# texto_plano = "8AB9CD0EF1AB2CDE"
# d = des()
# entrada = open('combinaciones.txt', 'r')
# salida = open('textos_cifrados.txt', 'w')
#
# for x in range(1, 100):
#     cyphered = d.encrypt(entrada.readline(x), texto_plano)
#     salida.write(cyphered)
#
# entrada.close()
# salida.close()

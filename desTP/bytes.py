decimal = 0
file = open('combinaciones.txt', 'a')
while True:
    bin_str = str(bin(decimal))
    bin_str = bin_str[2:len(bin_str)]
    if len(bin_str) < 24:
        for x in range(0, 24 - len(bin_str)):
            bin_str = '0' + bin_str[0:]
        if bin_str[7] == '0' and bin_str[15] == '0' and bin_str[-1] == '0':
            bin_str = bin_str[0:8] + '.' + bin_str[8:16] + '.' + bin_str[16:]
            file.write('00000000.00000000.00000000.00000000.00000000.' + bin_str + '\n')
    elif len(bin_str) == 24:
        if bin_str[7] == '0' and bin_str[15] == '0' and bin_str[-1] == '0':
            bin_str = bin_str[0:8] + '.' + bin_str[8:16] + '.' + bin_str[16:]
            file.write('00000000.00000000.00000000.00000000.00000000.' + bin_str + '\n')
    elif len(bin_str) > 24:
        break
    decimal = decimal + 1
file.close()

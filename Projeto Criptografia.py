#!/usr/bin/python3
# -*- coding: utf-8 -*-

TARGET = '01010011 01100101 01110010 01100101 01101001 00100000 01100001 01110000 01110010 01101111 01110110 01100001 ' \
         '01100100 01101111 00100000 01101110 01100101 01110011 01110100 01100001 00100000 01100100 01101001 01110011 '  
var: int = 0o1100011
var: int = 0o1101001
var = 0o1110000
var = 0o1101100
var = 0o1101001
var = 0o1101110
var = 0o1100001


frase = 'Serei aprovado nesta disciplina'
pre_a = [str(bin(ord(x))).replace('b', '') for x in frase]
a = [x if len(x) >= 8 else '0%s' % x for x in pre_a]
b = bin(int(''.join([str(ord(i)) for i in '3608']))).replace('b', '')

from operator import xor

# ord() converte para ASCII
# int() converte para inteiro
# bin() converte para binario

collected = list()

for i in a:
    # passamos cada letra de a na chave b
    collected.append(str(xor(int(b), int(i))))

a = collected  # o valor do loop anterior é volta a ser a
print(a)

newcollected = list()

for x in a:
    # passamos o valor do loop anterior por b novamente seu RU
    # o resultado é exatamente o valor de a lá do inicio
    newcollected.append(str(xor(int(b), int(x))))

valor_binario = [chr(int(y, 2)) for y in newcollected]  # C em binario
print()
print(''.join(valor_binario))  # C em binario convertido para ASCII e novamente para char comum

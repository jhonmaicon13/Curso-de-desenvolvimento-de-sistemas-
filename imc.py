#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura'))

imc = peso / (altura + altura)

print('Seu IMC é')
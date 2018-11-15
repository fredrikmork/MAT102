#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 10:42:19 2018

@author: fredrikgarsegmork
"""

import math
from RSA import eratosthenes, generate_primes, check_key, gcd, mult_inverse, RSA_encrypt, powermod, powermod2
print("Oppgave 1")
print("Oppgave a: \'bergen  '")
kod =[7040899, 18090405]
print ("Oppgave b: ",kod)
e = 1737
n = 160169311
T = kod
U = RSA_encrypt(n,e,T)
print("Oppgave c: ",U)

#lager en tabell med primtall mellom 2 og kvadratroten av n.
primTab = generate_primes(2, math.floor(math.sqrt(n)))
p = 0
q = 0
#finner p og q
for i in primTab:
    if n % i == 0:
        p = i
        q = math.floor(n / p)
print("Oppgave d:  p = ",p, "q = ", q)

      
print("Oppgave e: ",check_key(p, q, e))

U = [112718817, 85128008, 148479246, 91503316, 26066602, 95584344, 142943071]
d = mult_inverse(e,(p-1)*(q-1))
dekryptert = RSA_encrypt(n,d,U)
print("Oppgave f: ",dekryptert)

start = 0
s = ""
svar = ""
for delmengde in dekryptert:
    s = dekryptert[i]
    if (len(delmengde) % 2 == 1):
        s = "0" + str(dekryptert[i])
    add = 0
    for j in range(len(dekryptert)):
        add += 2
    svar += s[add:2]
print (chr(svar))
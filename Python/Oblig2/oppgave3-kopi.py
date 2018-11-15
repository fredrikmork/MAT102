#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 08:18:20 2018

@author: fredrikgarsegmork
"""
import numpy as np
import matplotlib.pyplot as plt
from pca import pca, meanCenter, standardize
#x=T*P+E


#E er en restmatrise, E tenker vi på som støy hvi vi har forklart mye av variasjonen.
Fylker = ['Akershus','Aust-Agder','Buskerud','Finnmark','Hedmark','Hordaland','Møre og Romsdal','Nordland','Nord-Trøndelag','Oppland','Oslo','Rogaland','Sogn og Fjordane','Sør- Trøndelag','Telemark','Troms','Vest-Agder','Vestfold','Østfold']
Indikatorer = ['Areal','Folketall', 'BNP/kapita','BNP/sysselsatt', 'Sysselsatte']
Areal = [4917.95,9155.36,14912.19,48631.38,27397.85,15436.98,15101.07,38478.13,22414, 25192.09,454.10,9376.77,18622.44,18848,15298.23,25876.85,7278.71,2225.38,4187.22]
Folketall =[604368,116673,279714,76149,196190,519963,266274,242866,137233,189479, 666759,472024,110266,317363,173307,165632,184116,247048,292893] 
BNPKap=[435982,337974,397080,438594,364944,488515,433030,428402,367157,363111, 820117,488463,455872,473954,371886,451887,403893,364007,331575]
BNPSyss =[918710,771973,831298,808765,777248,922939,834642,850163,759414,731136, 1125019,899272,846111,886057,817060,824648,811833,792748,778412] 
Sysselsatte=[270338,47868,125938,37143,86627,254290,127060,116020,62621, 86968,468375,233986,54490,166479,74749,84537,86997,106931,118320]

X = np.transpose(np.array([Areal,Folketall,BNPKap,BNPSyss,Sysselsatte]))
#E.T er transponerte av e

#Oppgave 3a
Xnorm = standardize(meanCenter(X))
print('Preprossessert X:')
print(Xnorm)

#Oppgave b
[T, P, E] = pca(Xnorm,a=2)
#T inneholder koordinatene til datapunktene i svaret, og hva en nxa-matrise- 
print(T)
#P inneholder retningene på de a aksene i m dimensjoner vi velger. det inneholder også koor til målretningene i svaret. P er en mxa-matrise(så den transponerte er axm)
print(P)

print('c):')
plt.figure(0)
plt.scatter(T[:, 0], T[:, 1])
for label, x, y in zip(Fylker, T[:, 0], T[:, 1]):
    plt.annotate(label, xy = (x, y), xytext = (5, -3),textcoords = 'offset points', ha = 'left')
plt.show()
print('c) Her ser vi dataene til fylkene')
plt.scatter(P[:, 0], P[:, 1])
for label, x, y in zip(Indikatorer, P[:, 0], P[:, 1]):
    plt.annotate(label, xy = (x, y), xytext = (5, -3),textcoords = 'offset points', ha = 'left')
plt.show()
plt.scatter(T[:, 0], T[:, 1])
for label, x, y in zip(Areal, T[:, 0], T[:, 1]):
    plt.annotate(label, xy = (x, y), xytext = (5, -3),textcoords = 'offset points', ha = 'left')
plt.show()
plt.scatter(T[:, 0], T[:, 1])
for label, x, y in zip(Folketall, T[:, 0], T[:, 1]):
    plt.annotate(label, xy = (x, y), xytext = (5, -3),textcoords = 'offset points', ha = 'left')
plt.show()
print('Her ser vi dataene til indikatorene')
print('Score plot: fylkene, Loading plot: indikatorene, ')
print('d) Oppland og Nord-trøndelag er de to fylkene som er mest like')
print('e) Oslo skiller seg klart ut. ')
print('f) Areal: Oslo, Finnmark og Nordland skiller seg ut')
print('g) En ekstra interessant opplysning: Oslo som er det minste fylket i areal, har flest innbyggere. Og Finnmark som er det største fylket i areal har minst folketall.')

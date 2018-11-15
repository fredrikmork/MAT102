#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 10:01:11 2018

@author: fredrikgarsegmork
"""
import numpy as np 
import matplotlib.pyplot as plt
#from scipy.interpolate import polyfit
from regression import linearRegression, quadraticRegression, cubicRegression

print('Oppgave 2 a): Grafen passer beskrivelsen meget.')
T=[13.14,12.89,12.26,12.64,12.22,12.47,12.51,12.80,12.24,12.77,13.35,12.82,13.57,13.38,14.41,14.00,15.68,15.41,15.51,15.86,15.72]
Tid=[0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60]
plt.scatter(Tid, T, label= 'tempScatter', color='k')

#Oppgave b)
#Linear reggression
[a, b] = linearRegression(Tid, T)
xplot = Tid
yplot = np.dot(a,xplot)+b
plt.plot(xplot, yplot, 'r')
#Determinant koeffisienten
Sy2 = sum((T-np.mean(T))**2)
SSELin = sum((T-np.dot(a,Tid)-b)**2)
r2Linear = (Sy2-SSELin)/Sy2
print('\nLineære regresjon sin determinant koeffisient:')
print(np.sqrt(r2Linear))
#print(np.corrcoef(Tid, T)[0][1])

#Oppgave c
#Quadratic regression
[a, b, c] = quadraticRegression(Tid, T)
yplot = np.dot(a,np.power(xplot,2))+np.dot(b,xplot) + c
plt.plot(xplot, yplot, 'b--')
#Determinant koeffisienten
Sy2 = sum((T-np.mean(T))**2)
SSEQuad = sum((T-(np.dot(a,np.power(Tid,2))+np.dot(b,Tid) + c))**2)
Quadratic = (Sy2-SSEQuad)/Sy2
print('\nKvadratisk regresjon sin determinant koeffisient:')
print(np.sqrt(Quadratic))
#print(np.corrcoef(xplot, yplot)[0][1])

#Cubic regression
[a, b, c, d] = cubicRegression(Tid, T)
yplot = np.dot(a,np.power(xplot,3))+ np.dot(b,np.power(xplot,2))+np.dot(c, xplot) + d
plt.plot(xplot, yplot, 'k')
#Determinant koeffisienten
SSECubic =sum((T-(np.dot(a,np.power(Tid,3))+np.dot(b,np.power(Tid,2))+np.dot(c,Tid) + d))**2)
r2Cubic = (Sy2-SSECubic)/Sy2
print('\nKubisk regresjon sin determinant koeffisient:')
print(np.sqrt(r2Cubic))
#print(np.corrcoef(xplot, yplot)[0][1])

plt.xlabel('Tid (m)')
plt.ylabel('Temperatur')
plt.title('Temperatur over tid')
plt.legend(['LReg','QReg', 'CReg', 'Temp'])
plt.show
#Oppgave d
print("\nKubisk regresjon passer grafen best fordi den scorer 96.6 prosent likhet til punktene, og følger punktene mer naturlig ")

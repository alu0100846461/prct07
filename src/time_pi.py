#! /usr/bin/python
#!encoding: UTF-8

#Importamos el módulo mod_pi.
import mod_pi

#Importamos las librerías necesarias.
import sys
import time

#Almacenamos el valor de referencia de pi con 35 decimales.
PI = 3.1415926535897931159979634685441852

#Definimos una t-upla que contiene distintas cantidades de subintervalos.
t_upla = (1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8)

#Inicializamos una lista vacía.
lista = []

#Almacenamos la hora anterior a la ejecución.
t0 = time.time()

#Llamamos sucesivamente a la función f (n) utilizando como argumentos los elementos de la t-upla.
for i in range (0, len(t_upla)):
    lista = lista + [mod_pi.f (t_upla[i])] 

#Definimos una función que imprime en forma de tabla los resultados obtenidos.
def show (lista):
    print "Iteración\tValor obtenido\tValor real\tError cometido"
    for j in range (0, len(lista)):
        print "%d\t\t%1.10g\t%1.10g\t%1.10f" %(j+1, lista[j], PI, abs(lista[j]-PI))

#Almacenamos la hora posterior a la ejecución.
tf = time.time()

#Imprimimos en pantalla la tabla de resultados.
show (lista)

#Mostramos en pantalla el tiempo total de ejecución.
print "El tiempo total de ejecución ha sido de %f segundos." %(tf - t0)


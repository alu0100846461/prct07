#! /usr/bin/python
#!encoding: UTF-8

#Importamos el módulo mod_pi.
import mod_pi

#Importamos la librería sys para permitir el uso de sys.argv.
import sys

#Almacenamos el valor de referencia de pi con 35 decimales.
PI = 3.1415926535897931159979634685441852

#Definimos una t-upla que contiene distintas cantidades de subintervalos.
t_upla = (1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8)

#Creamos una matriz con las dimensiones deseadas utilizando listas anidadas.
matrix = [None] * len(t_upla)
for i in range (len(t_upla)):
    matrix[i] = [None] * 3

#Llamamos sucesivamente a la función f (n) utilizando como argumentos los elementos de la t-upla, y almacenamos los resultados obtenidos en la matriz.
for i in range (len(t_upla)):
    matrix[i][0] = i + 1
    matrix[i][1] = mod_pi.f (t_upla[i])
    matrix[i][2] = abs(PI - matrix[i][1])

#Definimos una función que imprime en forma de tabla los resultados obtenidos.
def show (matrix):
    print "Iteración\tValor obtenido\tValor real\tError cometido"
    for j in range (0, len(t_upla)):
        print "%d\t\t%1.10g\t%1.10g\t%1.10f" %(matrix[j][0], matrix[j][1], PI, matrix[j][2])

#Imprimimos en pantalla la tabla de resultados.
show (matrix)


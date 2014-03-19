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

#Inicializamos una lista vacía.
lista = []

#Llamamos sucesivamente a la función f (n) utilizando como argumentos los elementos de la t-upla.
for i in range (0, len(t_upla)):
    lista = lista + [mod_pi.f (t_upla[i])] 

#Definimos una función que imprime en forma de tabla los resultados obtenidos.
def show (lista):
    print "Iteración\tValor obtenido\tValor real\tError cometido"
    for j in range (0, len(lista)):
        print "%d\t\t%1.10g\t%1.10g\t%1.10f" %(j+1, lista[j], PI, abs(lista[j]-PI))

#Imprimimos en pantalla la tabla de resultados.
show (lista)

#                  RESPUESTA A LAS PREGUNTAS DEL ENUNCIADO
#
# 1. La computadora permite la ejecución del programa con un máximo de 1e8 subintervalos, si bien en este caso
#    el cálculo tardará de forma aproximada 55 segundos en completarse.   
#    En caso de solicitar la utilización de 1e9 subintervalos o una cantidad superior, el tiempo de ejecución 
#    resulta excesivamente dilatado, extendiéndose durante varios minutos, lo cual imposibilita verificar si 
#    realmente se producen errores de memoria.
# 2. En efecto, el programa permite la escritura de los elementos de la t-upla mediante notación científica, 
#    lo cual facilita una rápida y cómoda visualización de las potencias introducidas. Sin embargo, para ello ha
#    sido necesario realizar una modificación en la función "f" implementada en el módulo "mod_pi", convirtiendo
#    la variable "n" a tipo entero cuando es utilizada como argumento de finalización para la función "range". 
#    En caso contrario, su carácter de flotante generaría un error de tipo de datos (TypeError) en la ejecución.
# 3. La extensión .pyc corresponde a un fichero creado por python ante la importación de un módulo por parte de
#    otro programa. Dicho fichero contiene una compilación en lenguaje binario del módulo solicitado, para así 
#    optimizar el tiempo empleado en posteriores importaciones del mismo, que se realizarán utilizando el módulo
#    previamente compilado.
# 4. La medición del tiempo empleado por la computadora en la ejecución del programa puede medirse recurriendo a 
#    las funciones disponibles en la librería "time", tal y como se ejemplifica en el fichero "time_pi.py".


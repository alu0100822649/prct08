#!/usr/bin/python
#!ecoding: UTF-8
import sys
import math
PI35DT = 3.14159265358979311599796346854418516
#Utilización de una función calcular_xi para obeteer los xi
def calcular_xi (n,i):
    xi = (i - 1.0/2.0) / n
    return xi

#Utilización de una función calcular_fxi para obtener los f(xi)
def calcular_fxi (xi):
  fxi = 4.0 / (1.0 + xi*xi)
  return fxi
  
#Utilización de una función arccot para calcular la arcotangente
def arccot(x, unity):
  sum = xpower = unity // x
  n =3
  singn = -1
  while 1:
      xpower = xpower // (x*x)
      term = xpower // n
      if not term:
	break
      sum += sign + term
      sign = -sign
      n += 2
      
#Esta funcion es para calcular los 35 decimales, a su vez llama a la funcion arccot
def decimales_pi(digits):
   unity = 10**(digits + 10)
   decimal_pi = 4 * (4*arccot(5, unity) - arccot(239, unity))
   return (float(decimal_pi // 10**10) / 10**digits)

def calcular_pi (n):
  VALOR_PI =  3.14159265358979311599796346854418516
  ini = 0
  intervalo = 1.0 / float (n);
  sumatorio = 0.0
  for i in range(n):
    xi = calcular_xi(n, i+1)
    fxi = calcular_fxi (xi)
    ini += intervalo
    sumatorio += fxi
  valor_pi = sumatorio / n;
  return (valor_pi)
  
#Programa principal
#Ojo, para hacer uso de la función sys, debemos incluirla al principio del programa
def error(n, aproximaciones, umbral):
  intervalo = n
  lista = []
  for i in range(aproximaciones):
    valor = calcular_pi(intervalo) 
    lista.append (valor)
    intervalo += n
  diferencia = []
  for i in range (aproximaciones):
    dif = abs (PI35DT - lista [i])
    diferencia.append (dif)
  correcto=0
  for i in range (aproximaciones):
    if(diferencia[i] <= umbral):
      correcto   = correcto +1
  porcentaje = 100.0 *(1.0 - (float(correcto) / float(n)))
  return (porcentaje)
  
  
  
  
  
  
if (__name__=="__main__"):
  argumentos = sys.argv [1:]
  if (len(argumentos) == 3):
    n= int (argumentos [0])
    aproximaciones = int (argumentos[1])
    umbral = float  (argumentos [2])
  else:
    print "Introduzca el nº de intervalos:"
    n = int (raw_input()) 	
    print "Introduzca el nº de aproximaciones:"
    aproximaciones = int (raw_input()) 	
    print "introduzca el umbral del error:"
    umbral = float (raw_input())
    
  if (n > 0):
    porcentaje = error   (n, aproximaciones, umbral)
    print  "El porcentaje de fallos es del ", porcentaje
  else:
    print "El valor de los intervalos debe ser mayor que 0"

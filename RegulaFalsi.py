#Falsa Posicion
import numpy as np

# INGRESO
fx = lambda x: x**(-x)-np.log(x)          #Ingresamos la funcion

a = 1                                     #Ingresamos el extremo inferior del Intervalo
b = 2                                     #Ingresamos el extremo superior del Intervalo
tolera = 0.00000000000001                 #Ingresamos la Tolerancia
# PROCEDIMIENTO
tabla = []                                #Definimos una lista vacia
tramo = abs(b-a)                          #Definimos "tramo" Como el valor absoluto de b-a
fa = fx(a)                                #Evaluamos f en el punto a
fb = fx(b)                                #Evaluamos f en el punto b
while not(tramo<=tolera):                 #Mientras que no se cumpla que
    c = b - fb*(a-b)/(fa-fb)              #Definimos de donde vamos a obtener a c
    fc = fx(c)                            #Evaluamos f en el punto c
    tabla.append([a,c,b,fa,fc,fb,tramo])  #Agregamos a "a", "c", "b", "fa", "fc", "fb" y "tramo" a la lista "tabla"
    cambio = np.sign(fa)*np.sign(fc)      #La funcion np.singn es una funcion que evalua el signo del numero, en este caso la funcion f evaluada en a y en c, devolviendo -1 si es menor a cero, 0 si es igual a eso y 1 si es mayor a cero
    if cambio>0:                          #si la multiplicacion de los signos es mayor a 0
        tramo = abs(c-a)                  #cambiamos "tramo" por el valor absoluto de c-a
        a = c                             #cambiamos a por c
        fa = fc                           #Cambiamos a fa por fc
    else:                                 #De lo contrario
        tramo = abs(b-c)                  #Cambiamos "tramo" por el valor absoluto de b-c
        b = c                             #Cambiamos "b" por "c"
        fb = fc                           #Cambiamos fb por fc
        
tabla = np.array(tabla)                   # Creamos una matriz con la lista de elementos " tabla "
ntabla = len(tabla)                       # la funcion " len () " de vuelveel numeros de elementos de un objeto

# SALIDA
np.set_printoptions(precision=4)          #Se establece el for para la impresion por filas de "tabla "
for i in range(0,ntabla,1):
    print('iteración:  ',i)
    print('[a,c,b]:    ', tabla[i,0:3])
    print('[fa,fc,fb]: ', tabla[i,3:6])
    print('[tramo]:    ', tabla[i,6])

print('raiz:  ',c)                        #Se imprime la el res ultado c
print('error: ',tramo)                    #se imprime el "tramo" o "error"
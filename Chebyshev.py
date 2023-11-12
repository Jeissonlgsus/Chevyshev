import matplotlib.pyplot as plt                                                 #es una interfaz basada en estado para matplotlib. Proporciona una forma de representación gráfica implícita, similar a MATLAB. También abre figuras en su pantalla y actúa como el administrador de GUI de figuras.
import numpy as np

num_nodes = int(input("Inserte el numero de nodos: "))                          #Entrada del Numero de Nodos
a=int(input("Inserte el extremo inferior del intervalo: "))                     #Ingreso del extremo inferior del intervalo
b=int(input("Inserte el extremo Superior del intervalo: "))                     #Ingreso del Extremo Superior del intervalo
interval = [a,b]                                                                #Se define el intervalo con "a" y "b" los extremos

def f(x):                                                                       #Se define una funcion "f(x)"
    return np.sin(x)                                                            #En esta linea, despues del return se pone la funcion a la que se desea aproximar con el formato de escritura de numpy, en este caso "np.sin(x)", que es el seno de x
def chebyshev_nodes(n, interval, closed_interval=False):                        #Definimos la funcion para calcular los nodos de Chabyshv
    i = np.arange(n)                                                            #Devuelve valores espaciados uniformemente dentro de un intervalo dado.
    if closed_interval:                                                         #Si el intervalo es cerrado
       x = np.cos((2*i)*np.pi/(2*(n-1)))                                        #Nodos en el intervalo cerrado [-1, 1]
    else:                                                                       #De lo contrario
       x = np.cos((2*i+1)*np.pi/(2*n))                                          #Nodos en el intervalo abierto (-1, 1)
    a, b = interval                                                             #Hace referencia a los dos extremos del intervalo
    return 0.5*(b - a)*x + 0.5*(b + a)                                          #Nodos en el intervalo [a, b]

def print_coefs(coefs):                                                         #Se define el formato de impresion de los coeficientes atraves de una funcion
    print("\nCoeficientes:")                                                    #Impresion de "Coeficientes:" con un salto de linea 
    for i in range(len(coefs)):                                                 #Para los i en el rango de los miembros de "Coef"
        print(f"    a_{i} = {coefs[i]:.14g}")                                   #Se imprimen los Coeficientes y el .14g o de .ng hace referencia a  Usa el formato exponencial si el exponente es menor que -4 o no menor que la precisión; de lo contrario, usa el formato decimal

def tics(interval, numtics):                                                    #Se define la funcion para particionar uniformemente el intervalo
    a, b = interval                                                             #Hace referencia a los dos extremos del intervalo
    return np.linspace(a, b, numtics)                                           #Devuelve números espaciados uniformemente en un intervalo específico.

def plot_func(x, y, err_abs, err_rel):                                          #Definimos una funcion para graficar
    fig, ax = plt.subplots(3)                                                   #Hacemos que haya 3 graficas en una misma
    fig.subplots_adjust(left=0.1, bottom=0.05, right=1, top=3, wspace=None, hspace=0.35) #Ajustamos los parametros de las subgraficas

    ax[0].plot(x, y, linewidth=1)                                               #Graficamos x y y y ajustamos el grosor de la linea
    ax[0].set_title('Funcion')                                                  #Ajustmos el nombre de la primer grafica
    ax[0].spines['left'].set_position('zero')                                   #Ajustamos a la izquierda la linea vertical que hara como nuestro eje y
    ax[0].spines['right'].set_color('none')                                     #Ajustamos que a la derecha no haya nada
    ax[0].spines['bottom'].set_position('zero')                                 #Centramos la linea vertical para que el origen cuadre
    ax[0].spines['top'].set_color('none')                                       #No deja nada en la parte superior de la grafica

#Se repiten las configuraciones anteriores para las siguientes dos graficas

    ax[1].plot(x, err_abs, linewidth=1)
    ax[1].set_title('Error absoluto del polinomio')
    ax[1].spines['left'].set_position('zero')
    ax[1].spines['right'].set_color('none')
    ax[1].spines['bottom'].set_position('zero')
    ax[1].spines['top'].set_color('none')   

    ax[2].plot(x, err_rel, linewidth=1)
    ax[2].set_title('Error relativo del polinomio')
    ax[2].spines['left'].set_position('zero')
    ax[2].spines['right'].set_color('none')
    ax[2].spines['bottom'].set_position('zero')
    ax[2].spines['top'].set_color('none')

    plt.show()

def test_errors(interval, poly_coefs, num_dots=1000):                           #definimos la funcion para Evaluar los errores
    x_dots = np.linspace(interval[0], interval[1], num_dots)                    #los x_dot son la distribucion desde 0 a 1 del intervalo
    y_dots = f(x_dots)                                                          #Evalua los x_dot en la funcion y los nombra y_dot
    y_poly_dots = np.polyval(poly_coefs, x_dots)                                #Toma los coeficientes y los x_dot y los evalua en el polinomio antraves de "np.Polynomial"

# Calculo errores

    err_abs = y_dots - y_poly_dots                                              #El error absoluto son los y_dots menos la evaluacion de los coeficientes y los x_dot 
    err_abs_max = max(np.abs(err_abs))                                          #Toma el valor maximo del error absoluto
    err_rel = np.arange(num_dots).astype(float)                                 #Devuelve valores espaciados uniformemente dentro del intervalo de los num:dots y lo comvierte al tipo float
    for i in range(len(x_dots)):                                                #Para cada i en el rango de los x_dots
        if y_dots[i] == 0:                                                      #si la i-esima componente de y_dots es igual a 0
            if y_poly_dots[i] == 0:                                             #Si la i-esima componente de y_poly_dots es igual a 0
                err_rel[i] = 0.0                                                #El error relativo en su i-sima componente es 0
            else:                                                               #De lo contrario 
                err_rel[i] = np.inf                                             #El error relativo en su i-esima componente es infinito
        else:                                                                   #De lo contrario
            err_rel[i] = err_abs[i] / y_dots[i]                                 #El error relativo en su i-esima componente es el error absoluto en su i-esima componente divido los y_dots en su i-esima componente
    err_rel_max = max(np.abs(err_rel))                                          #El Error relativo maximo es el maximo del valor absoluto del error relativo

# Impresion de los errores y maximos valores
    print(f"\nError Absoluto Maximo = {err_abs_max:.14g}")                      #Se imprime con salto de linea "Error absoluto" y el error absoluto maximo con el ajuste de lso decimales
    print(f"Maximo Error Relativo = {err_rel_max:.14g}")                        #Se imprime "Maximo error Relativo" con el ajuste de cifras decimales
    print(f"Maximo valor del polinomio = {max(y_poly_dots):.14g}")              #Se imprime el Valor maximo del polinomio con el ajuste de cifras
    print(f"Valor minimo del Polinomio= {min(y_poly_dots):.14g}")               #Se imprime el valos minimo del polinomio con el ajuste de las cifras
    plot_func(x_dots, y_dots, err_abs, err_rel)                                 #Llamamos la funcion "plot" para terminar las graficas

def main():                                                                     #Definimos la funcion main(), que actuara como la funcion principal, en las que se llamaran las demas una a una a convenencia de la logica expuesta anteriormente
    x_dots = chebyshev_nodes(num_nodes, interval, closed_interval=True)         #x_dots es el resultado de la funcion "chabyshex_Nodes"
    print(f"Nodos = {x_dots}")                                                  #Imprimimos los nodos encontrados anteriormente en un arreglo
    y_dots = f(x_dots)                                                          #los y_dots son los nodos evaluados en la funcion f(x)
    degrees = np.arange(1, num_nodes, 2)                                        # 2 = calcular solo coeficientes impares
    poly_coefs = np.polynomial.polynomial.polyfit(x_dots, y_dots, degrees)      #Llamamos "poly_coef" a usar la funcion np.polynomial.polynomial.polyfit, que es Ajuste por mínimos cuadrados de un polinomio a los datos. de los x_dot, y_dot y "degress"
    print_coefs(poly_coefs)                                                     #imprimimos el resultado anterior
    test_errors([0, interval[1]], np.flip(poly_coefs))                          #Llamamos la funcion "test_errors" desde 0 hasta el 1 en el intervalo y la matriz de coeficientes dada la vuelta con "Invierta el orden de los elementos en una matriz a lo largo del eje dado."
    plt.plot(x_dots,y_dots,'o')                                                 #Vamos a graficar en una grafica diferente la ubicacion de los nodos de Chebyshev
    plt.title('Grafica de la ubicacion de los Nodos de Chebyshev')              #Definimos el titulo de la grafica 
    plt.show()                                                                  #Mostramos lo anteriormente definido.

main()                                                                          #Es la invocacion de la funcion main()
from matplotlib import pyplot                                               
import numpy as np
import sympy as sym
n = 5 #cantidad de puntos
x = [-2,-1,0,1,2]
y = [1,2,3,3,4]
xc = [0,0,0,0,0]
xy = [0,0,0,0,0]
# sacamos los x_k cuadrados
for i in range(0,n):
  xc[i]=x[i]*x[i]
# sacamos los x*y  
for i in range(0,n):
  xy[i]=x[i]*y[i]
#sumamos los x_k, x_k^2,y_k y los x*y
sx = sum(x)
sy = sum(y)
sxc = sum(xc)
sxy = sum(xy)
#realizamos el despeje de a para sustituir y despejar b
b = (sy*sxc-sxy*sx)/(n*sxc-sx*sx)
#realizamos el despeje de a teniendo b
a = (sxy-b*sx)/(sxc)
#graficamos los puntos x_k y y_k
pyplot.plot(x,y,'o')
#=====================================================
# Función cuadrática.
def f1(x):
    return a*x+b
# Valores del eje X que toma el gráfico.
c = range(-10, 10)
# Graficar ambas funciones.
pyplot.plot(c, [f1(i) for i in c])
# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
# Limitar los valores de los ejes.
pyplot.xlim(-5, 5)
pyplot.ylim(0, 5)
# Guardar gráfico como imágen PNG.
pyplot.savefig("output.png")
# Mostrarlo.
pyplot.show()
#Tarea 3 Modelos Kaseng Fong 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from mpl_toolkits import mplot3d

#Parte 1 


xy = pd.read_csv("xy.csv",header = 0,index_col=0)

x = np.linspace(5,15,11)
y = np.linspace(5,25,21)

fy= np.sum(xy,axis=0)
fx= np.sum(xy,axis=1)



#Curva de mejor ajuste .Las dos figuras obtenidas eran una curva de Gauss

def gaussiana(x,mu,sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mu)**2/(2*sigma**2))

param_x,_=curve_fit(gaussiana,x,fx)
param_y,_=curve_fit(gaussiana,y,fy)

print(param_x)
print(param_y)





#Parte 3  

xyp = pd.read_csv("xyp.csv",header = 0)

#Correlacion
x_1 = xyp["x"] 
y_1 = xyp["y"] 
p_1 = xyp["p"]

correlation = 0 
for i in range(len(xyp)):
    correlation = correlation + x_1[i]*y_1[i]*p_1[i]; 
print( "La correlacion es :" ,correlation)


#Varianza 
covariance = correlation - (param_x[0]*param_y[0])
print( "La varianza es :" ,covariance)


# Coeficiente de varianza
cv = covariance/ (param_x[1]*param_y[1])
print( "El coeficiente de varianza es :" ,cv)




#Parte 4 

#Curva 3D
ax = plt.axes(projection='3d')
X1 = x_1
Y1 = y_1
Z1 = p_1

ax.plot_trisurf(X1, Y1, Z1, cmap='twilight_shifted')
ax.set_xlabel('X ')
ax.set_ylabel('Y ')
ax.set_zlabel('Z ')
ax.set_title('Curva 3D')
plt.show()


#Curva Fx
plt.xlabel('x')
plt.ylabel('Fx')
plt.title('Curva obtenida de datos en x')
plt.plot(x,fx)
plt.show()

#Curva Fy
plt.xlabel('y')
plt.ylabel('Fy')
plt.title('Curva obtenida de datos en y')
plt.plot(y,fy)
plt.show()

#Curva de mejor ajuste de los  valores de x
plt.xlabel('x')
plt.ylabel('Fx')
plt.title('Curva de mejor ajuste para datos de x')
plt.plot(x,gaussiana(x,param_x[0],param_x[1]))
plt.show()

#Curva de mejor ajuste de valores de y
plt.xlabel('y')
plt.ylabel('Fy')
plt.title('Curva de mejor ajuste para datos de y')
plt.plot(y,gaussiana(y,param_y[0],param_y[1]))
plt.show()



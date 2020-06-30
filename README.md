# Tarea 3 
# Variables aleatorias multiples
## Kaseng Fong 
## B42609



# Parte 1. 

Para obtener la mejor curva de ajuste para las funciones de las densidades marginales, a partir de los datos, se extrae los vectores mediante np.linspace los valores de las filas de X y las columnas de Y. Se extraen la sumatoria de cada columna y fila para la densidad marginal de X y Y  utilizando np.sum(), con estos datos se obtienen las graficas reales de las densidades marginales de Fx y Fy que se encuentran en la parte 4  del archivo. Seguidamente se procede a realizar el ajuste, donde se observa que el comportamiento de las graficas reales obtenidas representan una curva gaussiana, por lo que se define una funcion para obtener los parametros de "sigma" y "mu" donde se obtienen los siguientes parametros:

|        | X       | Y       |
|--------|---------|---------|
|![Equation](https://latex.codecogs.com/gif.latex?%5Csigma) | 3.2994  |  6.0269 |
|![Equation](https://latex.codecogs.com/gif.latex?%5Cmu)    | 9.90484 | 15.0794 |


``` python
xy = pd.read_csv("xy.csv",header = 0,index_col=0)

x = np.linspace(5,15,11)
y = np.linspace(5,25,21)

fy= np.sum(xy,axis=0)
fx= np.sum(xy,axis=1)

#Curva de mejor ajuste. 
def gaussiana(x,mu,sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mu)**2/(2*sigma**2))

param_x,_=curve_fit(gaussiana,x,fx)
param_y,_=curve_fit(gaussiana,y,fy)

print(param_x)
print(param_y)
```

# Parte 2
Partiendo de que existe indenpendencia entre X y Y, entonces se tiene que   
 ![equation](https://latex.codecogs.com/gif.latex?f_%7Bx%2Cy%7D%28x%2Cy%29%3D%20f_x%28x%29%5Ccdot%20f_y%28y%29)
 

De los resultados de la grafica, se observa que ambos representan una tendencia de una curva gaussiana, entonces: 
![equation](https://latex.codecogs.com/gif.latex?f%28x%29%3D%20ae%5E%7B%5Cfrac%7B-%28x-%5Cmu%29%5E2%7D%7B2%20%5Csigma%5E2%7D%7D)

![equation](https://latex.codecogs.com/gif.latex?f%28y%29%3D%20be%5E%7B%5Cfrac%7B-%28y-%5Cmu%29%5E2%7D%7B2%20%5Csigma%5E2%7D%7D)


entonces la expresion de la funcion de densidad conjunta esta dado por: 

![equation](https://latex.codecogs.com/gif.latex?f_%7Bx%2Cy%7D%28x%2Cy%29%3D%20abe%5E%7B%7B%5Cfrac%7B-%28x-%5Cmu%29%5E2%7D%7B2%20%5Csigma%5E2%7D%7D-%5Cfrac%7B-%28y-%5Cmu%29%5E2%7D%7B2%20%5Csigma%5E2%7D%7D)


sustituyendo los valores respectivos de  $\sigma$, $\mu$ para X y Y entonces se tiene que la funcion de densidad conjunta es:


![equation](https://latex.codecogs.com/gif.latex?f_%7Bx%2Cy%7D%28x%2Cy%29%3D%20abe%5E%7B%7B%5Cfrac%7B-%28x-9.9%29%5E2%7D%7B2%20*3.3%5E2%7D%7D-%5Cfrac%7B-%28y-15.07%29%5E2%7D%7B2*%206.02%5E2%7D%7D)

# Parte 3  


### 1. Correlacion : 
La correlacion indica cuanto grado de relacion estan asociados  linealmente una o mas variables. 
A partir  de los datos, se obtuvo una correlacion de 149.5428 entre las variables.

``` python
xyp = pd.read_csv("xyp.csv",header = 0)

#Correlacion
x_1 = xyp["x"] 
y_1 = xyp["y"] 
p_1 = xyp["p"]

correlation = 0 
for i in range(len(xyp)):
    correlation = correlation + x_1[i]*y_1[i]*p_1[i]; 
print( "La correlacion es :" ,correlation)

```


### 2. Covarianza:
La covarianza es una  medida  que indica cuanto puede cambiar de forma conjunta  dos variables aleatorias respecto a su medida, es decir, permite saber el comportamiento de una variable en funcion de la otra variable. La covarianza de la curva ajustada de los datos fue de  0.1831.

``` python

#Covarianza 
covariance = correlation - (param_x[0]*param_y[0])
print( "La covarianza es :" ,covariance)


```

### 3. Coeficiente de Covarianza:
El coeficiente de correlacion de Pearson, es el indice que mide el grado de covariacion entre distintas variables que se encuentren relacionadas linealmente, dicho valor debe de encontrarse entre -1 y 1.A partir de los datos se obtuvo que el coeficiente de correlacion es de 0.0092. 
``` python

# Coeficiente de covarianza
ccv = covariance/ (param_x[1]*param_y[1])
print( "El coeficiente de covarianza es :" ,ccv)


```


# Parte 4

## Curvas de las funciones de densidades marginales obtenidas de la parte 1. 


## 1. Curva de densidad marginal Fx
![image de pmfx](fx.png)
## 2. Curva de densidad marginal Fy
![image de mpmfy](fy.png)
## 3. Curva de  mejor ajuste para la densidad marginal Fx
![image de gaussx](ajustex.png)
## 4. Curva de mejor ajuste para la densidad marginal Fy
![iage de gaussy](ajustey.png)
## 5. Curva de densidad marginal conjunta
![image conjunta](3d.png)


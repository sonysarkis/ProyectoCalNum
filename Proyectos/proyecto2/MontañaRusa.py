import numpy as np  
import matplotlib.pyplot as plt  
from scipy.linalg import solve  # solve para resolver S.E. lineales


# Datos de la muestra
x_data = np.array([0, 1, 2, 3, 4, 5])   
y_data = np.array([0.5, 0.8, 1.0, 0.9, 1.2, 0.7])

# Valores para graficar la curva (100 puntos equidistantes entre 0 y 5)
x_vals = np.linspace(0, 5, 100) 

# Método para calcular los coeficientes del trazador cúbico sujeto
def coeficientes_trazCubic(x_data, y_data):
    cant_intervalos = len(x_data) - 1  # Número de intervalos entre los puntos de control
    xIntervalo = x_data[1:] - x_data[:-1]  # Diferencias entre puntos de control en el eje x
   
    matriz = np.zeros((cant_intervalos + 1, cant_intervalos + 1))  # Matriz del sistema de ecuaciones
    vector = np.zeros(cant_intervalos + 1)  # Vector del lado derecho del sistema de ecuaciones

    # Definir las ecuaciones del sistema
    matriz[0, 0] = 1  # Condición de frontera natural en el primer punto
    matriz[-1, -1] = 1  # Condición de frontera natural en el último punto
    
    for i in range(1, cant_intervalos):
        matriz[i, i-1] = xIntervalo[i-1]  # Coeficiente de la ecuación i-1
        matriz[i, i] = 2 * (xIntervalo[i-1] + xIntervalo[i])  # Coeficiente de la ecuación i
        matriz[i, i+1] = xIntervalo[i]  # coeficiente de la ecuación i+1
        vector[i] = 6 * ((y_data[i+1] - y_data[i]) / xIntervalo[i] - (y_data[i] - y_data[i-1]) / xIntervalo[i-1])  # Término independiente de la ecuación i

    # Resolver el sistema para obtener los coeficientes c
    coef_c = solve(matriz, vector)
    
    # Calcular los coeficientes a, b, d
    coef_a = y_data[:-1]  # Coeficientes a son los valores y_data excepto el último
    coef_b = (y_data[1:] - y_data[:-1]) / xIntervalo - xIntervalo * (2*coef_c[:-1] + coef_c[1:]) / 6  # Coeficiente b calculados a partir de a, h y c
    coef_d = (coef_c[1:] - coef_c[:-1]) / (6 * xIntervalo)  # Coeficiente d calculados a partir de c y h
    
    return coef_a, coef_b, coef_c[:-1], coef_d  # Devuelve los coeficientes calculados

# Coeficientes del trazador cúbico sujeto
coef_a, coef_b, coef_c, coef_d = coeficientes_trazCubic(x_data, y_data)

# Función del trazador cúbico sujeto
def evaluar_trazCubic(x, x_data, a, b, c, d):
    # Encuentra el intervalo en el que está x
    indice_intervalo = 0
    for i in range(len(x_data) - 1):
        if x_data[i] <= x < x_data[i + 1]:
            indice_intervalo = i
            break
    else:
        # Si x es igual al último punto de control
        if x == x_data[-1]:
            indice_intervalo = len(x_data) - 2
    
    # distancia desde x al punto de control más cercano
    x_dist = x - x_data[indice_intervalo]
    
    # valor interpolado usando los polinomios cúbicos
    return a[indice_intervalo] + b[indice_intervalo] * x_dist + c[indice_intervalo] * x_dist ** 2 + d[indice_intervalo] * x_dist ** 3

# Gráfica de los puntos de control y el trazador cúbico sujeto
plt.figure()
plt.plot(x_data, y_data, 'o', label='Puntos de control') 
plt.plot(x_vals, [evaluar_trazCubic(x, x_data, coef_a, coef_b, coef_c, coef_d) for x in x_vals], label='Trazador cúbico sujeto') 
plt.xlabel('x')  
plt.ylabel('y')  
plt.title('Trazador Cúbico Sujeto')  
plt.legend()  
plt.grid()  
plt.show()  






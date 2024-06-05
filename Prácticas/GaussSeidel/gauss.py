# Importamos las librerías necesarias
import numpy as np              # Para trabajar con matrices y vectores de manera eficiente
import matplotlib.pyplot as plt # Para crear gráficos

# Definimos la función GaussSeidel para resolver un sistema de ecuaciones lineales
def GaussSeidel(a, b, x_init=None, tolerance=1e-5, max_iterations=100):
    n = len(b) # Obtenemos el tamaño del vector b (número de ecuaciones)
    x = np.zeros_like(b) if x_init is None else x_init # Inicializamos el vector x con ceros o con un valor inicial dado
    
    # ciclo for para iterar un máximo de max_iterations veces
    for iteration in range(max_iterations):
        x_new = np.copy(x) # Creamos una copia del vector x para actualizar los valores
        for i in range(n):
            # Calculamos las sumas necesarias para la actualización de x[i]
            sum_before = np.dot(a[i, :i], x_new[:i])    # Suma de los elementos anteriores a i
            sum_after = np.dot(a[i, i+1:], x[i+1:])     # Suma de los elementos posteriores a i
            x_new[i] = (b[i] - sum_before - sum_after) / a[i, i] # Actualizamos x[i] con la fórmula de Gauss-Seidel
        
        # Calculamos la norma del error para ver si la solución es suficientemente precisa
        error_norm = np.linalg.norm(x_new - x) # Usamos la función norm de la librería numpy para calcular la norma del error
        
        # Si la norma del error es menor que la tolerancia, terminamos y devolvemos la solución
        if error_norm < tolerance:
            return x_new, iteration
        
        x = x_new # Actualizamos x con los nuevos valores
    
    return x, max_iterations # Si no hemos alcanzado la tolerancia, devolvemos la solución obtenida y el número máximo de iteraciones

# Función para graficar un vector
def graficar(vector):
    plt.figure(facecolor='lightblue') # Creamos una figura con fondo azul claro
    plt.plot(vector, 'go-', label='Gauss-Seidel') # Graficamos el vector con puntos verdes y líneas
    plt.title('Gauss-Seidel', fontweight='bold') # Ponemos un título en negrita al gráfico
    plt.xlabel('Índice', fontweight='bold') # Etiquetamos el eje x
    plt.ylabel('Valor', fontweight='bold') # Etiquetamos el eje y
    plt.legend() # Mostramos la leyenda del gráfico
    plt.show() # Mostramos el gráfico

# Definimos la matriz de coeficientes y el vector de términos independientes
a = np.array([[4, -1, 0, 0], 
              [-1, 4, -1, 0], 
              [0, -1, 4, -1], 
              [0, 0, -1, 3]], dtype=float)

b = np.array([15, 10, 10, 10], dtype=float)

# Llamamos a la función GaussSeidel con la matriz y el vector definidos
vector, iteraciones = GaussSeidel(a, b)

# Llamamos a la función para graficar el vector solución
# Análisis y Predicción de Datos Meteorológicos con Métodos de Interpolación

## Descripción del Proyecto

En este ejercicio, analizamos datos meteorológicos, específicamente temperaturas diarias en una ciudad a lo largo de una semana. Utilizamos diferentes métodos de interpolación para modelar y predecir estos datos. 
Los métodos de interpolación empleados son: interpolación de Taylor, interpolación de Lagrange, interpolación de Hermite e interpolación polinómica a trozos. 
Esto nos permite comparar la precisión y adecuación de cada método para datos meteorológicos.

## Estructura del Proyecto

### Parte 1: Interpolación de Taylor

1. **Generación de Datos:**
   - Se genera un conjunto de puntos que representan las temperaturas diarias en una ciudad durante una semana.
   
2. **Interpolación de Taylor:**
   - Implementación de la interpolación de Taylor en un punto específico para estos datos.
   - Gráfica de los datos originales y la interpolación de Taylor.

### Parte 2: Interpolación de Lagrange

1. **Generación de Datos:**
   - Se utilizan los mismos datos de temperaturas diarias generados anteriormente.
   
2. **Interpolación de Lagrange:**
   - Implementación de la interpolación de Lagrange para estos puntos.
   - Gráfica de los datos originales y la interpolación de Lagrange.

### Parte 3: Interpolación de Hermite

1. **Generación de Datos:**
   - Se utilizan los mismos datos de temperaturas diarias generados anteriormente, incluyendo derivadas aproximadas si es posible.
   
2. **Interpolación de Hermite:**
   - Implementación de la interpolación de Hermite para estos puntos.
   - Gráfica de los datos originales y la interpolación de Hermite.

### Parte 4: Interpolación Polinómica a Trozos

1. **Generación de Datos:**
   - Se utilizan los mismos datos de temperaturas diarias generados anteriormente.
   
2. **Interpolación Polinómica a Trozos:**
   - Implementación de la interpolación polinómica a trozos para estos puntos.
   - Gráfica de los datos originales y la interpolación polinómica a trozos.

## Instrucciones de Uso

### Prerequisitos

- Julia instalado en tu sistema.
- Paquetes necesarios: `SymPy`, `Interpolations`, `Plots`, `CSV`, `DataFrames`, `Statistics`.

### Pasos para Ejecutar el Código

1. **Preparación del Entorno:**
   - Instala los paquetes necesarios ejecutando:
     ```julia
     using Pkg
     Pkg.add("SymPy")
     Pkg.add("Interpolations")
     Pkg.add("Plots")
     Pkg.add("CSV")
     Pkg.add("DataFrames")
     Pkg.add("Statistics")
     ```

2. **Lectura de Datos:**
   - Coloca el archivo `temperaturas.csv` en el mismo directorio que el script de Julia.
   - El archivo `temperaturas.csv` debe contener los datos de temperaturas diarias en la primera columna y las temperaturas en las columnas subsiguientes.

3. **Ejecución del Script:**
   - Ejecuta el script de Julia que contiene el código completo para realizar las interpolaciones y generar las gráficas.
   - El script realiza las siguientes tareas:
     - Lee los datos del archivo CSV.
     - Calcula las interpolaciones de Taylor, Lagrange, Hermite y polinómica a trozos.
     - Grafica los resultados comparando los métodos de interpolación con los datos originales.

import numpy as np
import matplotlib.pyplot as plt

def GaussSeidel(a, b, x_init=None, tolerance=1e-5, max_iterations=100):
    n = len(b)
    x = np.zeros_like(b) if x_init is None else x_init
    for iteration in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            sum_before = np.dot(a[i, :i], x_new[:i])
            sum_after = np.dot(a[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - sum_before - sum_after) / a[i, i]
        error_norm = np.linalg.norm(x_new - x)
        if error_norm < tolerance:
            return x_new, iteration
        x = x_new
    return x, max_iterations

def graficar(vector):
    plt.figure(facecolor='lightblue')
    plt.plot(vector, 'go-', label='Gauss-Seidel')
    plt.title('Gauss-Seidel', fontweight='bold')
    plt.xlabel('Índice', fontweight='bold')
    plt.ylabel('Valor', fontweight='bold')
    plt.legend()
    plt.show()

vector, iteraciones = GaussSeidel(
    np.array([[4, -1, 0, 0], [-1, 4, -1, 0], [0, -1, 4, -1], [0, 0, -1, 3]], dtype=float),
    np.array([15, 10, 10, 10], dtype=float)
)

graficar(vector)
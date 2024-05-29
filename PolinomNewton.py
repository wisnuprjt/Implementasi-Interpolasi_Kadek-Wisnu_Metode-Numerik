import numpy as np
import matplotlib.pyplot as plt

def newton_interpolation(x, y, x_values):
    # Menghitung divided differences
    n = len(x)
    divided_diff = np.zeros((n, n))
    divided_diff[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i, j] = (divided_diff[i + 1, j - 1] - divided_diff[i, j - 1]) / (x[i + j] - x[i])

    # Menghitung nilai polinomial di titik-titik x_values
    def P(x_point):
        result = divided_diff[0, 0]
        term = 1.0
        for i in range(1, n):
            term *= (x_point - x[i - 1])
            result += divided_diff[0, i] * term
        return result
    
    return [P(xi) for xi in x_values]

# Data dari gambar
x = [5, 10, 15, 20, 25, 30, 35, 40]
y = [40, 30, 25, 40, 18, 20, 22, 15]

# Titik-titik untuk menguji interpolasi
x_test = np.linspace(5, 40, 500)
y_test = newton_interpolation(x, y, x_test)

# Titik-titik interpolasi untuk ditampilkan pada grafik (pilih beberapa secara manual)
x_interpolasi = [7, 12, 17, 22, 27, 32, 37]
y_interpolasi = newton_interpolation(x, y, x_interpolasi)

# Plot hasil interpolasi
plt.figure(figsize=(10, 6))
plt.plot(x_test, y_test, label='Polinomial Newton')
plt.scatter(x, y, color='red', label='Titik yang diketahui')
plt.scatter(x_interpolasi, y_interpolasi, color='green', label='Titik interpolasi', zorder=5)
plt.title('Interpolasi Polinomial Newton')
plt.xlabel('Tegangan, x (kg/mm²)')
plt.ylabel('Waktu patah, y (jam)')
plt.legend()
plt.grid(True)
plt.show()

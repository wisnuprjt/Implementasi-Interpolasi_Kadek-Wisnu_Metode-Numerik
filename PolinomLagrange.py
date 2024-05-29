import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, x_values):
    def L(k, x_point):
        L_k = 1
        for i in range(len(x)):
            if i != k:
                L_k *= (x_point - x[i]) / (x[k] - x[i])
        return L_k
    
    def P(x_point):
        result = 0
        for k in range(len(y)):
            result += y[k] * L(k, x_point)
        return result

    return [P(xi) for xi in x_values]

# Data dari gambar
x = [5, 10, 15, 20, 25, 30, 35, 40]
y = [40, 30, 25, 40, 18, 20, 22, 15]

# Titik-titik untuk menguji interpolasi
x_test = np.linspace(5, 40, 500)
y_test = lagrange_interpolation(x, y, x_test)

# Titik-titik interpolasi untuk ditampilkan pada grafik (pilih beberapa secara manual)
x_interpolasi = [7, 12, 17, 22, 27, 32, 37]  # Titik-titik yang dipilih secara manual
y_interpolasi = lagrange_interpolation(x, y, x_interpolasi)

# Plot hasil interpolasi
plt.figure(figsize=(10, 6))
plt.plot(x_test, y_test, label='Polinomial Lagrange')
plt.scatter(x, y, color='red', label='Titik yang diketahui')
plt.scatter(x_interpolasi, y_interpolasi, color='green', label='Titik interpolasi', zorder=5)
plt.title('Interpolasi Polinomial Lagrange')
plt.xlabel('Tegangan, x (kg/mm²)')
plt.ylabel('Waktu patah, y (jam)')
plt.legend()
plt.grid(True)
plt.show()

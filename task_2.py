import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функція, яку інтегруємо
def f(x):
    return x**2

# Межі інтегрування
a = 0
b = 2

# Метод Монте-Карло для обчислення інтеграла
def monte_carlo_integration(func, a, b, n_points=10000):
    x_random = np.random.uniform(a, b, n_points)
    y_values = func(x_random)
    integral_estimate = (b - a) * np.mean(y_values)
    return integral_estimate

# Аналітичне обчислення інтегралу
analytical_result, error = quad(f, a, b)

# Монте-Карло обчислення
mc_result = monte_carlo_integration(f, a, b)

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
plt.grid(True)
plt.show()

print("Інтеграл методом Монте-Карло:", mc_result)
print("Аналітичне значення (quad):", analytical_result)
print("Похибка:", error)

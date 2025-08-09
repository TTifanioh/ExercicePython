import matplotlib.pyplot as plt
import numpy as np

# As you use numpy, you can immediately use the numpy instead of creating it manually

def f_1(x_var):
    return np.where((x_var >= 0) & (x_var < 1), x_var, np.where((x_var >= 1) & (x_var <= 2), 1, np.nan))

def f_2(x_var):
    return np.sin(x_var) + 0.1

x_min, x_max, step = 0, 2, 0.05
x = np.arange(x_min, x_max + step, step)

y1 = f_1(x)
y2 = f_2(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y1, label='Graph of function 1', color='blue', linewidth=2)
plt.plot(x, y2, label='Graph of function 2', color='red', marker='*', linestyle='None')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Functino graphs')
plt.legend()
plt.grid(True)
plt.xlim(x_min, x_max)
plt.ylim(0, 1.5)
plt.tight_layout()
plt.show()

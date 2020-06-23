import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure(figsize=(6, 6))
plt.xlim(-10, 10)
plt.ylim(-10, 10)

ax = plt.gca()

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

for x in range(-10, 11):
    for y in range(-10, 11):
        try:
            # m = math.e ** x - math.pi ** y
            # m = x * y
            # m = x ** y
            # m = 2 * x / y
            # m = math.log(x)
            # m = math.log(abs(x))
            m = (-1) * x / y
            x_bound = 0.3 * math.cos(math.atan(m))
            ax.plot(np.linspace(x - x_bound, x + x_bound, 999),
                    m * (np.linspace(x - x_bound, x + x_bound, 999) - x) + y,
                    c='r', linewidth='0.75')
        except ZeroDivisionError:
            pass
        except ValueError:
            pass

plt.tight_layout()
plt.show()

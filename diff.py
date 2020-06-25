import matplotlib.pyplot as plt
import numpy as np
from math import *


def create_slope_field(x_range, y_range):

    if x_range > y_range:
        fig = plt.figure(figsize=(12, y_range / x_range * 12))
    else:
        fig = plt.figure(figsize=(x_range / y_range * 6, 6))

    plt.xlim((-1) * x_range, x_range)
    plt.ylim((-1) * y_range, y_range)

    ax = plt.gca()

    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    plt.xticks(np.arange((-1) * x_range, x_range + 1, 1.0))
    plt.yticks(np.arange((-1) * y_range, y_range + 1, 1.0))

    ax.tick_params(axis='both', labelsize=5)

    for x in range((-1) * x_range, x_range + 1):
        for y in range((-1) * y_range, y_range + 1):
            try:
                m = x + y
                # m = cos(y)
                # m = e ** x - pi ** y
                # m = x * y
                # m = x ** y
                # m = 2 * x / y
                # m = log(x)
                # m = log(abs(x))
                # m = (-1) * x / y
                reach = 0.3 * cos(atan(m))
                ax.plot(np.linspace(x - reach, x + reach, 999),
                        m * (np.linspace(x - reach, x + reach, 999) - x) + y,
                        c='#960a00', linewidth='1')
            except ZeroDivisionError:
                ax.scatter(x, y, s=10, c='#0307fc')
                pass
            except ValueError:
                ax.scatter(x, y, s=10, c='#0307fc')
                pass

    plt.tight_layout()
    plt.show()


def main():

    x_range = int(input("Please input the max x value: "))
    y_range = int(input("Please input the max y value: "))

    print()
    print("Slope lines will be red ticks and points where the slope is undefined will be highlighted in blue.")

    query = bool(input("Do you understand? (press enter): "))
    create_slope_field(x_range, y_range)


if __name__ == "__main__":
    main()

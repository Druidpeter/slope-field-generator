import matplotlib.pyplot as plt
import numpy as np
import math


def create_slope_field(x_low, x_high, y_low, y_high):
    fig = plt.figure(figsize=(6, 6))
    plt.xlim(x_low, x_high)
    plt.ylim(y_low, y_high)

    ax = plt.gca()

    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    for x in range(x_low, x_high + 1):
        for y in range(y_low, y_high + 1):
            try:
                # Recommended sample differential equations for testing.                
                # m = math.e ** x - math.pi ** y
                # m = x * y
                # m = x ** y
                m = 2 * x / y
                # m = math.log(x)
                # m = math.log(abs(x))
                # m = (-1) * x / y
                
                # Establishes how far the tick marks can "reach" beyond their respective points.
                reach = 0.3 * math.cos(math.atan(m))
                ax.plot(np.linspace(x - reach, x + reach, 999),
                        m * (np.linspace(x - reach, x + reach, 999) - x) + y,
                        c='r', linewidth='1')
            except ZeroDivisionError:
                pass
            except ValueError:
                pass

    plt.tight_layout()
    plt.show()


def main():
    x_low = int(input("Please enter the lower x-axis bound: "))
    x_high = int(input("Please enter the upper x-axis bound: "))
    y_low = int(input("Please enter the lower y-axis bound: "))
    y_high = int(input("Please enter the upper y-axis bound: "))
    create_slope_field(x_low, x_high, y_low, y_high)


if __name__ == "__main__":
    main()

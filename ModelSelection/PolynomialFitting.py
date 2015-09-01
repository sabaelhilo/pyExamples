import numpy as np
import matplotlib.pyplot as plt


def plot_polynomials(x, y, num):
    figure1 = plt.figure(num)
    rect = figure1.patch
    rect.set_facecolor('white')
    ax = figure1.add_subplot(1, 1, 1)

    # Plot data and polynomials
    ax.plot(x, y, 'o', label="data")
    xp = np.linspace(0, 3, 100)
    for order in range(3, 11, 3):
        p = np.poly1d(np.polyfit(x, y, order))
        ax.plot(xp, p(xp), '-', label="order %d" % order)

    plt.ylim(-2, 2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='upper right')
    plt.ylim(-2, 2)


x1 = np.arange(0, 3, 0.2)
y1 = [0.3, 0.6, 0.7, 1.1, 0.75, 1.3, 0.55, 0.59, -0.5, -0.60, -1.4, -1.3, -0.55, -0.6, 0.1]


plot_polynomials(x1, y1, 1)

p = np.poly1d(np.polyfit(x1, y1, 3))
x2 = np.linspace(0, 3, 100)
pure = np.array(p(x2))
noise = np.random.normal(0, 0.3, pure.size)

plot_polynomials(x2, pure + noise, 2)

plt.show()


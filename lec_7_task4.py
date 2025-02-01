import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_points(x0, y0, C, D, n):
    X = np.zeros(n)
    Y = np.zeros(n)
    X[0] = x0
    Y[0] = y0

    for i in range(1, n):
        X[i] = X[i-1]**2 - Y[i-1]**2 + C
        Y[i] = 2 * X[i-1] * Y[i-1] + D

    return X, Y

def animate(i):
    ax.clear()
    ax.scatter(X[:i+1], Y[:i+1], color='blue')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_title('Фрактальное множество')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

x0, y0 = 0.1, 0.1
C, D = 0.3, 0.33
n_points = 100

X, Y = generate_points(x0, y0, C, D, n_points)

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=n_points, interval=100)
plt.show()




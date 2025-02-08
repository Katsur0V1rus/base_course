import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def create_square(angle):
    square = np.array([[1, 1], [-1, 1], [-1, -1], [1, -1], [1, 1]])
    rotation = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle), np.cos(angle)]])
    rotated_square = square.dot(rotation)
    return rotated_square

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
line, = ax.plot([], [], 'b-')


def init():
    line.set_data([], [])
    return line,

def update(frame):
    angle = np.radians(frame)  
    square = create_square(angle)
    line.set_data(square[:, 0], square[:, 1])
    return line,

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 2), init_func=init, blit=True)
ani.save('rotating_square.gif', writer='pillow', fps=30)

plt.show()

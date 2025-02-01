import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Создание пространства и подпространства для анимации
fig, ax = plt.subplots()

# Обьект анимации
anim_object, = plt.plot([], [], '-', lw=2) 
x, y = [], [] # Координаты обьекта анимации
frames_interval = np.linspace(0, 2*np.pi, 100)

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)

# Функция подстановки параметра в обьект анимации
def update(frame):
    x.append(frame)
    y.append(np.sin(frame))

    #Передача координат обьекту анимации
    anim_object.set_data(x, y)

    return anim_object

ani = FuncAnimation(fig, update, frames=frames_interval, interval=50) # Вызов пространства для анимации, вызов функции подпространства координат,интервал значений, интервал между кадрами, по умолчанию 200 милисикунд
ani.save('animation_l.gif', writer="pillow")
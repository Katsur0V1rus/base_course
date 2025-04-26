import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

latitude = 20     # широта 
azimuth = 200    # азимут 
hour_angle = -50  # часовой угол рт)

lat = np.radians(latitude)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2*np.pi, 50)
v = np.linspace(0, np.pi, 50)
xs = np.outer(np.cos(u), np.sin(v))
ys = np.outer(np.sin(u), np.sin(v))
zs = np.outer(np.ones_like(u), np.cos(v))
ax.plot_wireframe(xs, ys, zs, color='gray', alpha=0.3)

ax.set_box_aspect([1,1,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

point, = ax.plot([], [], [], 'ro', markersize=8)
text = ax.text(0,0,0,"", color='blue')


def update(h_angle):
    
    h_rad = np.radians(h_angle)

    x = np.cos(lat) * np.cos(h_rad)
    y = np.cos(lat) * np.sin(h_rad)
    z = np.sin(lat)
    point.set_data([x], [y])
    point.set_3d_properties([z])
    text.set_position((x, y))
    text.set_3d_properties(z)
    text.set_text(f'h={int(h_angle)}')
    return point, text

ani = FuncAnimation(fig, update, frames=np.linspace(-180, 180, 120), interval=100, blit=True)

plt.show()
plt.savefig('fig_9.png')
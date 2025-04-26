import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

latitude = 70  # широта, градусы
declination = 70  # склонение, градусы
hour_angle = 15  # часовой угол, градусы

lat_rad = np.radians(latitude)
dec_rad = np.radians(declination)
ha_rad = np.radians(hour_angle)

h = np.arcsin(np.sin(lat_rad)*np.sin(dec_rad) + np.cos(lat_rad)*np.cos(dec_rad)*np.cos(ha_rad))

cos_A = (np.sin(dec_rad) - np.sin(h)*np.sin(lat_rad)) / (np.cos(h)*np.cos(lat_rad))

sin_A = -np.cos(dec_rad)*np.sin(ha_rad) / np.cos(h)  
A = np.arctan2(sin_A, cos_A)

r = 1
x = r * np.cos(h) * np.cos(A)
y = r * np.cos(h) * np.sin(A)
z = r * np.sin(h)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

xs = np.outer(np.cos(u), np.sin(v))
ys = np.outer(np.sin(u), np.sin(v))
zs = np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(xs, ys, zs, color='green', alpha=0.3, edgecolor='blue')

ax.scatter(x, y, z, color='red', s=100, label='Точка (широта=70, склонение=70, часовой угол=15)')

ax.set_box_aspect([1,1,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Точка на сфере')

ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])

ax.legend()
plt.show()
plt.savefig('fig_6.png')
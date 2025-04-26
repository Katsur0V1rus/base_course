import numpy as np
import matplotlib.pyplot as plt

latitude = 20      # широта в градусах
azimuth = 200      # азимут в градусах
hour_angle = -50   # часовой угол (просто вывод)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

R = 5
phi = np.linspace(0, 2*np.pi, 100)
theta = (0, np.pi, 100)
x = R * np.outer(np.cos(phi), np.sin(theta))
y = R * np.outer(np.sin(phi), np.sin(theta))
z = R * np.outer(np.ones(np.size(phi))np.cos(theta))
ax.plot_wireframe(xs, ys, zs, color='blue', alpha=0.5)

ax.scatter(x, y, z, color='red', s=100)

ax.text(x, y, z, f' h={hour_angle}', color='black')

ax.set_box_aspect([1,1,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
plt.savefig('fig_8.png')
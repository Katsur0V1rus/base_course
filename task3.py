import numpy as np
import matplotlib.pyplot as plt

latitude = 20       # широта
azimuth = 200       # азимут 
hour_angle = -50    # часовой угол 

lat_rad = np.radians(latitude)
az_rad = np.radians(azimuth)
hour_angle_rad = np.radians(hour_angle)

x = np.cos(lat_rad) * np.cos(az_rad)
y = np.cos(lat_rad) * np.sin(az_rad)
z = np.sin(lat_rad)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

xs = np.outer(np.cos(u), np.sin(v))
ys = np.outer(np.sin(u), np.sin(v))
zs = np.outer(np.ones_like(u), np.cos(v))

ax.plot_surface(xs, ys, zs, color='lightblue', alpha=0.3, edgecolor='red')

hour_angle_norm = (hour_angle + 180) / 360  
color = plt.cm.viridis(hour_angle_norm)

ax.scatter(x, y, z, color=color, s=100, label=f'Широта={latitude}, Азимут={azimuth}, Часовой угол={hour_angle}')

ax.set_box_aspect([1,1,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Точка на сфере с широтой, азимутом и часовым углом')
ax.legend()

plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Данные
latitude = 20      # широта в градусах
azimuth = 200      # азимут в градусах
hour_angle = -50   # часовой угол (просто вывод)

# Переводим градусы в радианы для вычислений
lat = np.radians(latitude)
azi = np.radians(azimuth)

# Считаем координаты точки на сфере радиуса 1
x = np.cos(lat) * np.cos(azi)
y = np.cos(lat) * np.sin(azi)
z = np.sin(lat)

# Создаем фигуру и 3D ось
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Рисуем сферу (тонкая сетка)
u = np.linspace(0, 2*np.pi, 30)
v = np.linspace(0, np.pi, 30)
xs = np.outer(np.cos(u), np.sin(v))
ys = np.outer(np.sin(u), np.sin(v))
zs = np.outer(np.ones_like(u), np.cos(v))

ax.plot_wireframe(xs, ys, zs, color='gray', alpha=0.5)

# Отмечаем точку красным цветом
ax.scatter(x, y, z, color='red', s=100)

# Подписываем точку часового угла
ax.text(x, y, z, f' H={hour_angle}°', color='black')

# Оси и пропорции, чтобы сфера была круглая
ax.set_box_aspect([1,1,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
plt.savefig('fig_7.png')

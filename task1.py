import numpy as np
import matplotlib.pyplot as plt

# Данные
latitude = 70  # широта
declination = 70  # склонение
hour_angle = 15  # стандартночасовой угол

# Переводим углы в радианы для вычислений
lat_rad = np.radians(latitude)
dec_rad = np.radians(declination)

# Создаем диапазон часовых углов от -180 до 180 с шагом 1 градус
hour_angles = np.radians(np.arange(-180, 181, 1))

# Формула для вычисления высоты тела над горизонтом:
# sin(h) = sin(lat)*sin(dec) + cos(lat)*cos(dec)*cos(hour_angle)
h = np.arcsin(np.sin(lat_rad) * np.sin(dec_rad) + np.cos(lat_rad) * np.cos(dec_rad) * np.cos(hour_angles))

# Переводим высоту в градусы
h_deg = np.degrees(h)

# Рисуем движение (высоту) тела в зависимости от часового угла
plt.figure(figsize=(10,5))
plt.plot(np.degrees(hour_angles), h_deg, label='Движение тела')

# Отмечаем точку при стандартночасовом угле 15°
h_15 = np.arcsin(np.sin(lat_rad) * np.sin(dec_rad) + np.cos(lat_rad) * np.cos(dec_rad) * np.cos(np.radians(hour_angle)))
plt.scatter(hour_angle, np.degrees(h_15), color='red', label=f'Точка при час. угле {hour_angle}°')

plt.title('Движение тела на небе')
plt.xlabel('Часовой угол (градусы)')
plt.ylabel('Высота тела (градусы)')
plt.grid(True)
plt.legend()
plt.show()
  

plt.savefig('fig_5.png')

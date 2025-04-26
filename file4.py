import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}) 

R = 5 


ax.scatter(5,0,0, "o", color="r")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Сфера с экваториальными и горизонтальными координатами')
ax.legend()

ax.set_aspect('equal')  

plt.savefig('fig_4.png')

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import axes3d

plt.style.use('_mpl-gallery')

# Make data
X, Y, Z = axes3d.get_test_data(0.05)

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

ax.scatter(5, 0, 0, '0', colour = 'r')

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.savefig('fig_3.png')
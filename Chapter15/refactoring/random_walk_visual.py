import matplotlib.pyplot as plt

from random_walk import RandomWalk


rw = RandomWalk(5_000)
rw.fill_walk()

plt.style.use('bmh')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.gnuplot,
    edgecolors='none', s=3)
ax.set_aspect('equal')

ax.scatter(0, 0, c='green', edgecolors='none', s=50)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=50)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
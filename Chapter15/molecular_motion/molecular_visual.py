import matplotlib.pyplot as plt

from molecular_motion_walk import RandomWalk

rw = RandomWalk(5_000)
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(16,9))

ax.plot(rw.x_values, rw.y_values, c='green', linewidth=5)
ax.set_aspect('equal')

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


plt.show()
import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [y ** 3 for y in x_values]

fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=3)

plt.show()
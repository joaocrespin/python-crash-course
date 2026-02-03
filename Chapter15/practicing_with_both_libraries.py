import matplotlib.pyplot as plt
import plotly.express as px
from die import Die
from modified_random_walks.random_walk import RandomWalk

# Mathplotlib
first_die = Die(6)
second_die = Die(6)

y_values = [0 for _ in range(0, first_die.num_sides + second_die.num_sides + 1)]
for roll_num in range(10_000):
    result = first_die.roll() + second_die.roll() 
    y_values[result] += 1

print(y_values)
y_values = y_values[2:]
print(y_values)

max_result = first_die.num_sides + second_die.num_sides 
x_values = [i for i in range(2, max_result + 1)]

print(x_values)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.step(x_values, y_values, where='mid')
plt.xticks(x_values)

ax.set_title('2d6 Rolls', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Recurrence', fontsize=14)

plt.show()

# Plotly Express
rw = RandomWalk(5_000)
rw.fill_walk()
point_numbers = range(rw.num_points)

title = 'Random Walk in Plotly'
labels = {'x': '', 'y': ''}

fig = px.scatter(x=rw.x_values, y=rw.y_values, color=point_numbers,
    color_continuous_scale='Viridis', title=title, labels=labels)
fig.show()
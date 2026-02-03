import plotly.express as px
from die import Die

first_die = Die(8)
second_die = Die(8)

results = []

for roll_num in range(50_000):
    result = first_die.roll() + second_die.roll()
    results.append(result)

frequencies = []
max_result = first_die.num_sides + second_die.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

fig = px.bar(x=poss_results, y=frequencies)
fig.show()
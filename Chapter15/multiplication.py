import plotly.express as px
from die import Die

first_die = Die(6)
second_die = Die(6)

results = []

for roll_num in range(10_000):
    result = first_die.roll() * second_die.roll() 
    results.append(result)

frequencies = []
max_result = first_die.num_sides * second_die.num_sides 
poss_results = range(1, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Rolling two D6s and multiplying the results"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick = 1)
fig.show()
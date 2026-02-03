import plotly.express as px
from die import Die

first_die = Die(6)
second_die = Die(6)

results = [first_die.roll() + second_die.roll() for _ in range(50_000)]

max_result = first_die.num_sides + second_die.num_sides 
poss_results = range(2, max_result + 1)
frequencies = [results.count(value) for value in poss_results]

title = "Rolling two D6s"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.line(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick = 1)
fig.show()
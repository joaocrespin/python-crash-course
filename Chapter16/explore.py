from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt


path = Path('Chapter16/weather_data/san_francisco_2025_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

date_index = header_row.index('DATE')
time_index = header_row.index('TOBS')
name_index = header_row.index('NAME')

dates, tobs = [], []
place_name = ""
for row in reader:
    place_name = row[name_index]
    current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    try:
        tob = int(row[time_index])
    except ValueError:
        continue
    else:
        dates.append(current_date)
        tobs.append(tob)

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(dates, tobs, color='purple', alpha=0.5)

ax.set_title(f'Average {place_name}\nTime of Observation', fontsize=16)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel('Time', fontsize=16)
ax.tick_params(labelsize=12)

plt.show()
from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt


path = Path('Chapter16/weather_data/san_francisco_2025_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

date_index = header_row.index('DATE')
high_temp_index = header_row.index('TMAX')
low_temp_index = header_row.index('TMIN')
name_index = header_row.index('NAME')

dates, highs, lows = [], [], []
place_name = ""
for row in reader:
    place_name = row[name_index]
    current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    try:
        high = int(row[high_temp_index])
        low = int(row[low_temp_index])
    except ValueError:
        continue
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='gray', alpha=0.1)

ax.set_title(f'{place_name} Temperatures', fontsize=16)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=12)

plt.show()
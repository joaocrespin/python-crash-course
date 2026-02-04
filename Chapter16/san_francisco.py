from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt


path = Path('Chapter16/weather_data/san_francisco_2025_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[5], '%Y-%m-%d')
    high = int(row[6])
    low = int(row[8])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title('San Francisco Temperatures', fontsize=16)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=12)

plt.show()

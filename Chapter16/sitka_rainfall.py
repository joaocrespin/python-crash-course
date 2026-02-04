from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt

path = Path('Chapter16\weather_data\sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

rainfall, dates = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    rain = float(row[5])
    dates.append(current_date)
    rainfall.append(rain)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, color='blue', alpha=0.5)

ax.set_title('Sitka Rainfall Amounts, 2021', fontsize=16)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel('Pluviosity', fontsize=16)
ax.tick_params(labelsize=12)

plt.show()

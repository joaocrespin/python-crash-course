from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt

def get_data(path, dates, highs, lows, date_index, high_index, low_index):
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

sitka_path = Path('Chapter16\weather_data\sitka_weather_2021_simple.csv')
sitka_dates,  sitka_highs, sitka_lows = [], [], []
get_data(sitka_path, sitka_dates, sitka_highs, sitka_lows, 2, 4, 5)

ax.plot(sitka_dates, sitka_highs, color='red', alpha=0.6)
ax.plot(sitka_dates, sitka_lows, color='blue', alpha=0.6)
ax.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue', alpha=0.15)

path = Path('Chapter16\weather_data\death_valley_2021_simple.csv')
death_valley_dates, death_valley_highs, death_valley_lows = [], [], []
get_data(path, death_valley_dates, death_valley_highs, death_valley_lows,
    2, 3, 4)

ax.plot(death_valley_dates, death_valley_highs, color='red', alpha=0.3)
ax.plot(death_valley_dates, death_valley_lows, color='blue', alpha=0.3)
ax.fill_between(death_valley_dates, death_valley_highs, death_valley_lows,
    facecolor='blue', alpha=0.05)

ax.set_title('Sitka X Death Valley Temperatures', fontsize=16)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(labelsize=12)
ax.set_ylim(10, 140)

plt.show()
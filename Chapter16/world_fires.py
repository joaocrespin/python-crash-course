from pathlib import Path
import csv
import plotly.express as px

path = Path('Chapter16/eq_data/world_fires_1_day.csv')
contents = path.read_text(encoding='utf-8')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

latitude_index = header_row.index('latitude')
longitude_index = header_row.index('longitude')
brightness_index = header_row.index('brightness')

latitude, longitude, brightness = [], [], []
for row in reader:
    try:
        lat = float(row[latitude_index])
        lon = float(row[longitude_index])
        bri = float(row[brightness_index])
    except ValueError:
        continue
    else:
        latitude.append(lat)
        longitude.append(lon)
        brightness.append(bri)

fig = px.scatter_geo(lat=latitude, lon=longitude, size=brightness, 
        title='World Fires',
        color=brightness,
        color_continuous_scale='peach',
        labels={'color':'Brightness'},
        projection='natural earth',
    )
fig.show()
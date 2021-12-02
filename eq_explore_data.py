import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data
filename = 'data/eq_data_1_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

magnitudes, lons, lats, texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    magnitudes.append(mag)
    lons.append(lon)
    lats.append(lat)
    texts.append(title)

# Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons, 
    'lat': lats,
    'text': texts,
    'marker': {
        'size': [5*mag for mag in magnitudes],
        'color': magnitudes,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
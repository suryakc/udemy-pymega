import pandas
import folium

file_data = pandas.read_csv("Volcanoes.txt")
data_subset = file_data[['LAT', 'LON']]
data = [tuple(x) for x in data_subset.values]

map = folium.Map()

fg = folium.FeatureGroup(name="Pune Home Map")

for coordinates in data:
    fg.add_child(folium.Marker(location=coordinates, popup="Pune Home", icon=folium.Icon(color='blue')))
map.add_child(fg)


map.save("VolcanoMap.html")
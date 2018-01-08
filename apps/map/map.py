import folium
import pandas

#map = folium.Map(location=[18.566007, 73.816620], zoom_start=90, tiles='OpenStreetMap')
''' fg = folium.FeatureGroup(name="Pune Home Map")

for coordinates in [[18.566007, 73.816620], [18, 73], [19, 74]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Pune Home", icon=folium.Icon(color='blue')))
map.add_child(fg)
map.save("FirstMap.html") '''

map = folium.Map()

fg = folium.FeatureGroup(name="Pune Home Map")

for coordinates in [[18.566007, 73.816620], [18, 73], [19, 74]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Pune Home", icon=folium.Icon(color='blue')))
map.add_child(fg)


map.save("FirstMap.html")


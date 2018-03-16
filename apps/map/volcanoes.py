import pandas
import folium
import numpy

file_data = pandas.read_csv("Volcanoes.txt")
data_subset = file_data[['LAT', 'LON', 'ELEV']]
data = [tuple(x) for x in data_subset.values]

def get_color(elevation):
    if elevation < 1000:
        return 'blue'
    if elevation < 2000:
        return 'green'
    return 'yellow'

map = folium.Map()

fg = folium.FeatureGroup(name="Volcano Map")

for volcano in data:
    popup_color = get_color(volcano[-1].item())
    volcano_icon = folium.Icon(color=popup_color) 
    #fg.add_child(folium.Marker(location=volcano[0:2], popup=str(volcano[-1]) + ' m', icon=volcano_icon))
    fg.add_child(folium.CircleMarker(location=volcano[0:2], radius=6, 
        color='grey', fill=True, fill_color=popup_color, fill_opacity=0.7, popup=str(volcano[-1]) + ' m'))

fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))
map.add_child(fg)


map.save("VolcanoMap.html")

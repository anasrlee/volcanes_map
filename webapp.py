import folium
import pandas as pd
import os
import json

map=folium.Map(location=[37,10], zoom_start=4, attr="Mapbox Bright")
df=pd.read_csv("world_volcanes.csv")

lat=df["lat"]
lon=df["lon"]
elev=df["elevation"]


def color_production(elev):
    if elev <1000 :
        return 'green'
    elif 1000<=elev<3000 :
        return 'orange'
    else :
        return 'red'

fgv=folium.FeatureGroup(name="volcano")
for lt , ln ,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el)+" m", radius=6 ,fill_color=color_production(el), color='grey',fill_opacity=1))


with open('world.json',encoding='utf-8-sig', errors='ignore') as f:
     data = json.load(f, strict=False)


fgp = folium.FeatureGroup(name="gouvernorat")
fgp.add_child(folium.GeoJson(data, style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("index.html")

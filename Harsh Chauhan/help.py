import folium

m = folium.Map([51.5, -0.25], zoom_start=10)

test = folium.Html('<b>Hello world</b>', script=True)

popup = folium.Popup(test, max_width=2650)
folium.RegularPolygonMarker(
    location=[51.5, -0.25], popup=popup,
).add_to(m)

m.save('./templates/osm.html')
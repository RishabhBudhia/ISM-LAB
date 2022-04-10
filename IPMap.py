import geocoder
import folium

## public ip
g = geocoder.ip("me")
myAddress = g.latlng

myMap1 = folium.Map(location=myAddress,zoom_start=12)
folium.CircleMarker(location=myAddress,radius=50,popup="India").add_to(myMap1)
folium.Marker(myAddress,popup="Vellore").add_to(myMap1)
myMap1.save("MapIPOutput.html")
print(myAddress)
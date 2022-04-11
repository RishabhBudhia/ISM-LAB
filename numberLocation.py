import phonenumbers
import folium


from myNumber import number

from phonenumbers import geocoder

sanNumber = phonenumbers.parse(number)
## opencagedata.com api - https://opencagedata.com/
Key = "174dc01731054d33a0b0a0c5414a573d"
yourLocation = geocoder.description_for_number(sanNumber,"en");
print(yourLocation)

## get service provider
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat,lng],zoom_start=9)

folium.Marker([lat,lng],popup=yourLocation).add_to((myMap))

## save map in html file

myMap.save("myLocation.html")
import requests
import json
import googlemaps
from geopy.distance import geodesic

url = "https://api.vuumly.com/api/availableDevices"
availableVehiclesJson = requests.get(url, stream = False)
availableVehicles = json.loads(availableVehiclesJson.text)

origin = input("Ievadiet sākuma lokāciju: ")
destination = input("Ievadiet galamērķi: ")

gmaps = googlemaps.Client(key="AIzaSyBHcAg-O9jXgFnyLLwYwN-j4sSLavKsRas")
geocode_origin = gmaps.geocode(origin)
originCoordinates = geocode_origin[0]["geometry"]["location"]
originCoordinates = (originCoordinates["lat"], originCoordinates["lng"])

for vehicle in availableVehicles[:]:
    vehicleLoaction = (vehicle["location"]["lat"], vehicle["location"]["lng"])
    geodesic(vehicleLoaction, originCoordinates).km
    vehicle["distance"] = geodesic(vehicleLoaction, originCoordinates).km
    if vehicle["distance"] > 1.0:
        availableVehicles.remove(vehicle)

print(availableVehicles)

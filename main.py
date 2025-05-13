import requests
import json
import googlemaps
from geopy.distance import geodesic

url = "https://api.vuumly.com/api/availableDevices"
availableVehiclesJson = requests.get(url, stream = False)
availableVehicles = json.loads(availableVehiclesJson.text)
availableCars = []
availableScooters = []

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
    else:
        directionsToVehicle = gmaps.directions(origin, vehicleLoaction, mode = "walking")
        vehicle["walk_time"] = directionsToVehicle[0]["legs"][0]["duration"]["value"]
        if vehicle["device_type"] == "car":
            directionsToDestination = gmaps.directions(vehicleLoaction, destination, mode = "driving")
            vehicle["drive_duration"] = directionsToDestination[0]["legs"][0]["duration"]["value"]
            availableCars.append(vehicle)
        elif vehicle["device_type"] == "scooter":
            directionsToDestination = gmaps.directions(vehicleLoaction, destination, mode = "walking")
            vehicle["ride_duration"] = directionsToDestination[0]["legs"][0]["duration"]["value"]
            availableScooters.append(vehicle)

#print(availableScooters)
#print(gmaps.directions(origin, destination, mode = "driving")[0]["legs"][0]["duration"]["value"])

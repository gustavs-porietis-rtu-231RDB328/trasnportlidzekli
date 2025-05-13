import requests
import json

url = "https://api.vuumly.com/api/availableDevices"
availableVehiclesJson = requests.get(url, stream = False)
availableVehicles = json.loads(availableVehiclesJson.text)

#for vehicle in availableVehicles:
    #print(vehicle["distinct_place"])

origin = input("Ievadiet sākuma lokāciju: ")
destination = input("Ievadiet galamērķi: ")


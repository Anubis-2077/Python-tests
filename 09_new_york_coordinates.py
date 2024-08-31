import requests
import json

url = "https://nominatim.openstreetmap.org/search"

params = {
    "q": "New York, USA",
    "format": "json",
    "polygon_geojson": 1
}

response = requests.get(url, params=params)
data = response.json()


if data:
    ny_data = {
        "name": data[0]["display_name"],
        "bounding_box": data[0]["boundingbox"],
        "geojson": data[0]["geojson"]
    }
    
    with open ('new_york_data.json', 'w') as json_file:
        json.dump(ny_data, json_file)
        
        
        print("datos guardados en el archivo json")
        
else:
    print("No se encontraron resultados")
import requests

from geopy.geocoders import Nominatim


def get_address(latitude, longitude):
    #    base_url = "https://nominatim.openstreetmap.org/reverse"
    #    params = {
    #        "lat": latitude,
    #        "lon": longitude,
    #        "format": "json",
    #    }
    #    response = requests.get(base_url, params=params)
    #    print(response.status_code)
    #    print(response.text)
    #    if response.status_code == 200:
    #        return response.address.country
    #    else:
    #        return "Fields"
    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.reverse((latitude, longitude))
    return location.address.rpartition(',')[-1]


def get_satellite_image(latitude, longitude, zoom, size, api_key):
    base_url = "https://maps.googleapis.com/maps/api/staticmap"
    params = {
        "center": f"{latitude},{longitude}",
        "zoom": zoom,
        "size": size,
        "maptype": "satellite",
        "key": api_key
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        image_url = response.url
        print(f"L'URL de l'image satellite est: {image_url}")
    else:
        print("Erreur lors de la récupération de l'image satellite:", response.status_code, response.text)


if __name__ == "__main__":
    api_key = "AIzaSyD4l7piytpD0xeI9gDLpCMN-_pSVAQSejk"
    latitude, longitude = 6.398150, -1.000507
    recolte_type = "cacao"
    print("tu es expert en agriculture, tu as pour mission d'analyser une image satellite de champs de " + "recol" + " au " + get_address(latitude, longitude) +
          " afin de prévenir l'apparition de différents parasites ("
          "champignon, maladie, insectes). tes réponses sont composées de la position de la zone à traiter, du parasite en question et d'un solution de "
          "traitement possible. répond de manière concise et précise, si tu ne trouve pas c'est qu'il n'y a rien.")
    get_satellite_image(latitude, longitude, 18, "640x640", api_key)

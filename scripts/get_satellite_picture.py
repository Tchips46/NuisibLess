import requests


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
        print(f"{image_url}")
    else:
        print("Error:", response.status_code, response.text)


if __name__ == "__main__":
    api_key = "AIzaSyD4l7piytpD0xeI9gDLpCMN-_pSVAQSejk"
    latitude, longitude = 6.398150, -1.000507
    get_satellite_image(latitude, longitude, 18, "640x640", api_key)

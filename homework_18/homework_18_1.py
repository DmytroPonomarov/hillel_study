import random
import requests

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": "20",  # щоб було з чого вибрати
}

response = requests.get(search_url, params=search_params)
data = response.json()

items = data.get("collection").get("items")

nasa_ids = []
for item in items:
    data_info = item.get("data")
    nasa_id = data_info[0].get("nasa_id")
    nasa_ids.append(nasa_id)

urls = []
for nasa_id in nasa_ids:
    asset_search_url = f"{BASE_URL}/asset/{nasa_id}"
    asset_response = requests.get(asset_search_url)
    if asset_response.status_code == 200:
        asset_urls = asset_response.json()
        links = asset_urls.get("collection").get("items")
        for link in links:
            url = link.get("href")
            if url.endswith(".jpg"):
                urls.append(url)

selected_links = random.sample(urls, k=2)
first_link = selected_links[0]
second_link = selected_links[1]

first_photo_response = requests.get(first_link).content
first_photo_name = "mars_photo1.jpg"
with open(f"{first_photo_name}", "wb") as handler:
    handler.write(first_photo_response)

second_photo_response = requests.get(second_link).content
second_photo_name = "mars_photo2.jpg"
with open(f"{second_photo_name}", "wb") as handler:
    handler.write(second_photo_response)

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


def rover_search():
    response = requests.get(search_url, params=search_params)
    data = response.json()
    items_dict = data.get("collection").get("items")
    return items_dict


def nasa_ids_search(items_dict):
    nasa_ids = []
    for item in items_dict:
        data_info = item.get("data")
        nasa_id = data_info[0].get("nasa_id")
        nasa_ids.append(nasa_id)
    return nasa_ids


def images_url_search(nasa_ids):
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
    return first_link, second_link


def download_image(link: str, file_name: str):
    response = requests.get(link).content
    with open(file_name, "wb") as handler:
        handler.write(response)

if __name__ == "__main__":
    items = rover_search()
    nasa_ids = nasa_ids_search(items)
    first_link, second_link = images_url_search(nasa_ids)
    download_image(first_link, "mars_photo1.jpg")
    download_image(second_link, "mars_photo2.jpg")

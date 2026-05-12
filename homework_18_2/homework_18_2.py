import requests

BASE_URL = "http://127.0.0.1:8080"
IMAGE = "mars_photo1.jpg"
EXPECTED_URL = f"{BASE_URL}/uploads/{IMAGE}"

# POST
def post_function(url: str, image: str, expected_url = EXPECTED_URL):
    with open(image, "rb") as file:
        files = {"image": file}
        post_response = requests.post(f"{url}/upload", files=files)

    response_dict_post = post_response.json()
    assert post_response.status_code == 201
    assert response_dict_post["image_url"] == expected_url

# GET
def get_function(url: str, image: str, expected_url = EXPECTED_URL):
    headers = {"Content-Type": "text"}
    get_response = requests.get(f"{url}/image/{image}", headers=headers)
    response_dict_get = get_response.json()
    assert get_response.status_code == 200
    assert response_dict_get["image_url"] == expected_url

# DELETE
def delete_function(url: str, image: str):
    delete_response = requests.delete(f"{url}/delete/{image}")
    delete_response_dict = delete_response.json()
    assert delete_response.status_code == 200
    assert delete_response_dict["message"] == f"Image {image} deleted"

post_function(BASE_URL, IMAGE)
get_function(BASE_URL, IMAGE)
delete_function(BASE_URL, IMAGE)
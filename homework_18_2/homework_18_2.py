import requests

BASE_URL = "http://127.0.0.1:8080"
IMAGE = "mars_photo1.jpg"
EXPECTED_URL = f"{BASE_URL}/uploads/{IMAGE}"

# POST
with open(IMAGE, "rb") as file:
    files = {"image": file}
    post_response = requests.post(f"{BASE_URL}/upload", files=files)

response_dict_post = post_response.json()
assert post_response.status_code == 201
assert response_dict_post["image_url"] == EXPECTED_URL

# GET
headers = {"Content-Type": "text"}

get_response = requests.get(f"{BASE_URL}/image/{IMAGE}", headers=headers)
response_dict_get = get_response.json()
assert get_response.status_code == 200
assert response_dict_get["image_url"] == EXPECTED_URL

# DELETE
delete_response = requests.delete(f"{BASE_URL}/delete/{IMAGE}")
delete_response_dict = delete_response.json()
assert delete_response.status_code == 200
assert delete_response_dict["message"] == f"Image {IMAGE} deleted"

import requests
from config.settings import API_BASE_URL
from config.settings import build_headers

def get_categories():
    url = f"{API_BASE_URL}/categories"
    response = requests.get(url, headers=build_headers())

    if response.status_code == 200:
        data = response.json()
        # return [c["name"] for c in data]
        return [{"id": c["id"], "name": c["name"]} for c in data]
    else:
        print("Error HTTP:", response.status_code)
        return []
    
    
def create_post(token, post_data):
    url = f"{API_BASE_URL}/posts/create"

    try:
        response = requests.post(url, json=post_data, headers=build_headers(token))
        return response
    except Exception as e:
        print(f"❌ Error de conexión al crear el post: {e}")
        return None

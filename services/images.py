from config.settings import UNSPLASH_ACCESS_KEY, API_BASE_URL
import requests
import random
import tempfile
import os

def get_profile_image(token, sex):
    image_url = search_profile_image(sex)
    if not image_url:
        return None
    
    image_file_path = save_profile_image(image_url)
    if not image_file_path:
        return None
    
    response = upload_image(token, image_file_path)
    
    os.remove(image_file_path)
    
    if response.status_code == 200:
        print("✅ Imagen subida con éxito")
        return response.json().get("path")
    else:
        print("❌ Error al subir la imagen")
        return None

def search_profile_image(sex):
    url = f"https://api.unsplash.com/photos/random?query={sex}&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["urls"]["regular"]
    else:
        print("Error HTTP:", response.status_code)
        print("📄 Texto:", response.text)
        return ""

def save_profile_image(image_url):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
            temp_file.write(response.content)
            temp_file.close()
            return temp_file.name
        else:
            print("Error al descargar la imagen:", response.status_code)
            return None
    except Exception as e:
        print("Error al guardar la imagen:", e)
        return None
    
def upload_image(token, image_path):
    url = f"{API_BASE_URL}/media/image/upload"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        'User-Agent': 'BloogolBot/1.0'
    }
    files = {
        "profile_image": open(image_path, "rb")
    }
    response = requests.post(url, files=files, headers=headers)
    return response

def get_post_image(prompt):
    url = f"https://api.unsplash.com/search/photos"
    params = {
        "query": f"{prompt}",
        "per_page": 20,
        "page": 1,
        "orientation": "landscape",
    }
    
    response = requests.get(url, headers={"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}, params=params)
    data = response.json()

    if data["results"]:
        imagen = random.choice(data["results"])
        return imagen["urls"]["regular"]
    else:
        return ""
import requests
import random
from faker import Faker
from config.settings import API_BASE_URL, build_headers
from services.ia import get_description
from services.images import get_profile_image
from generators.posts import create_post_and_publish

faker = Faker('es_ES')
user_tokens = {}

def create_user():
    sex = random.choice(["female", "male"])
    name = faker.first_name_male() if sex == "male" else faker.first_name_female()
    last_name = faker.last_name()
    email = faker.email()
    
    payload = {
        "name": name,
        "last_name": last_name,
        "email": email,
        "password": "password",
    }
    
    response = requests.post(f"{API_BASE_URL}/register", json=payload, headers=build_headers())
    
    if response.status_code == 201:
        print("✅ Usurio creado con éxito")
    else:
        print("❌ Error al crear el usuario")
        return

    user_tokens[email] = {
        "id": response.json()["user"]["id"],
        "token": response.json()["token"],
    }

    bio = get_description(name, sex)
    image = get_profile_image(user_tokens[email]["token"], sex)
    
    update_profile(user_tokens[email]["token"], user_tokens[email]["id"], name, last_name, email, bio, image)
    
    for _ in range(10):
        try:
            create_post_and_publish(user_tokens[email])
        except Exception as e:
            continue

    
    
def update_profile(token, id, name, last_name, email, bio, image):
    payload = {
        "name": name,
        "last_name": last_name,
        "email": email,
        "bio": bio,
        "profile_image": image,
    }
        
    response = requests.put(f"{API_BASE_URL}/users/{id}/profile", json=payload, headers=build_headers(token))
    if response.status_code == 200:
        print("✅ Perfil actualizado con éxito")
    else:
        print("❌ Error al actualizar el perfil")
import requests
import random 
from services.images import get_post_image
from utils.delta import convert_to_delta
from services.api import get_categories
from services.api import create_post
from services.ia import generate_post

def create_post_and_publish(user):
    categories = get_categories()
    if not categories:
        print("No hay categorías disponibles")
        return
    
    category = random.choice(categories)
    
    result = generate_post(category["name"])
    title = result["title"]
    description = result["description"]
    content = result["content"]
    prompts = result["prompts"]
    
    images = [get_post_image(p) for p in prompts]
    delta = convert_to_delta(content, images)
    
    post_data = {
        "user_id": user["id"],
        "category_id": category["id"],
        "title": title,
        "content": description,
        "html": delta,
        "image": images[0],
        "image_urls": images,
        "is_published": True,
    }
    
    response = create_post(user["token"], post_data)

    if response and response.status_code == 201:
        print("✅ Post creado con éxito")
    else:
        print(f"❌ Error al crear el post ({response.status_code if response else 'sin respuesta'})")

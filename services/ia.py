import openai
from config.settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_description(name, gender):
    rol = "una mujer" if gender == "female" else "un hombre"
    prompt = f"Escribe una descripción de perfil para {rol} llamado/a {name}, en español, no más de 20 palabras como primera persona."
    response = openai.responses.create(
        model="gpt-3.5-turbo",
        input=prompt,
    )
    
    return response.output_text.strip()

def generate_post(category):
    prompt = (
        f"Escribe un post de blog en español sobre {category}. "
        "Incluye un título, de 4 a 6 párrafos completos, y subtítulos breves en español (máximo 8 palabras y sin punto final) distribuidos a lo largo del contenido. "
        "Los subtítulos deben estar intercalados de forma natural entre algunos párrafos, no todos al principio ni al final. "
        "Al final del post, agrega exactamente 3 prompts en inglés para generar imágenes realistas relacionadas con el contenido. "
        "Sigue exactamente este formato sin agregar explicaciones ni encabezados adicionales:\n\n"
        "Título:\n...\n\nContenido:\n...\n\nPrompts de imagen:\n...\n...\n..."
    )
    
    response = openai.responses.create(
        model="gpt-4o-mini",
        input=prompt,
    )
    
    text = response.output_text
    
    sections = text.split("Contenido:\n")
    title = sections[0].replace("Título:\n", "").strip()
    parts = sections[1].split("Prompts de imagen:\n")

    paragraphs = [p.strip() for p in parts[0].split("\n") if p.strip()]
    prompts = [p.replace("-", "").strip() for p in parts[1].split("\n") if p.strip()]
    
    return {
        "title": title,
        "description": parts[0].replace("\n", "").strip(),
        "content": paragraphs,
        "prompts": prompts,
    }
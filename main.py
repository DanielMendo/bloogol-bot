from services.api import get_categories
from services.ia import get_description
from services.images import get_profile_image
from services.images import get_post_image
from generators.users import create_user
from utils.delta import convert_to_delta
from generators.posts import create_post

# print(get_categories())
# print(get_description("Daniel", "male"))
# print(get_profile_image("woman"))
# print(get_post_image("inteligencia artificial"))
create_user()
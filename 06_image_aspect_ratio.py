#
 # Crea un programa que se encargue de calcular el aspect ratio de una
 # imagen a partir de una url.
 # - Url de ejemplo:
 #   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 # - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 #   imagen de 1920#1080px.
 #
 
import requests
from PIL import Image
from io import BytesIO
from math import gcd


def get_and_load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        image = Image.open(BytesIO(response.content))
        
        return image
    except requests.RequestException as e:
        print(f'error al cargar al descargar la imagen: {e}')
    except IOError as e:
        print( f'no se pudo abrir la imagen: {e}')
        
        
def calculate_aspect_ratio(image):
    if image:
        
        width, height = image.size
        divisor = gcd(width, height)
        return f'{width//divisor}:{height//divisor}'
    
        
        
url = "https://preview.redd.it/le-ped%C3%AD-a-dalle-2-que-haga-un-carpincho-tomando-mate-con-un-v0-w5kmf0v19bf91.png?width=1024&format=png&auto=webp&s=3688a3b063954b3d28959e71bd206ddfba6de2cf"
imagen = get_and_load_image(url)
if imagen:
    imagen.show()
    aspect_ratio = calculate_aspect_ratio(imagen)
    print('Aspect ratio:', aspect_ratio)
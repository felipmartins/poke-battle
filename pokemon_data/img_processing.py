from requests import get

def get_sprite(name, url):
    img_data = get(url).content
    with open('pokemon_data/static/pokemon/'+str(name)+'.jpg', 'wb') as handler:
        handler.write(img_data)
    
    return img_data
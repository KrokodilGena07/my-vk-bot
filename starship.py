import requests


def get_starship():
    starships = []
    for i in range(2, 17):
        response = requests.get(f'https://swapi.dev/api/starships/{i}').json()
        starships.append(response)

    max_atmospheric_speed = {
        'max_atmospheric_speed': starships[0]['max_atmosphering_speed'],
        'name': starships[0]['name']
    }

    for starship in starships:
        try:
            if int(starship['max_atmosphering_speed']) > int(max_atmospheric_speed['max_atmospheric_speed']):
                max_atmospheric_speed = {
                    'max_atmospheric_speed': starship['max_atmosphering_speed'],
                    'name': starship['name']
                }
        except (KeyError, ValueError):
            continue
    return max_atmospheric_speed['name']
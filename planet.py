import requests


def get_planet():
    planets = []
    for i in range(2, 10):
        response = requests.get(f'https://swapi.dev/api/planets/{i}').json()
        planets.append(response)

    max_diameter_planet = {'diameter': planets[0]['diameter'], 'name': planets[0]['name']}

    for planet in planets:
        if int(planet['diameter']) > int(max_diameter_planet['diameter']):
            max_diameter_planet = {'diameter': planet['diameter'], 'name': planet['name']}
    return max_diameter_planet['name']
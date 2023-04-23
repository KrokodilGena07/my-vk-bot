import requests
from bs4 import BeautifulSoup


def get_games(game_genre):
    game_list = []
    result_list = []

    url = 'https://store.steampowered.com/?l=russian'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    game_items = soup.find_all('div', class_='tab_item_content')

    for game_item in game_items:
        current_tag_list = []
        game_name = game_item.find('div', class_='tab_item_name')
        top_tags = game_item.find_all('span', class_='top_tag')
        for top_tag in top_tags:
            current_tag_list.append(top_tag.text)
        game_list.append({'name': game_name.text, 'description': current_tag_list})

    for game in game_list:
        for item in game['description']:
            if game_genre.lower() in item.lower():
                result_list.append(game['name'])

    if result_list:
        return result_list
    return 'Игр не найдено!'
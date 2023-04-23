from starship import get_starship
from wiki import get_info_wiki
from planet import get_planet
from game import get_games
from course import get_course


def get_response(message):
    response = None

    for command in command_dict:
        if command in message:
            response = command_dict.get(command)()

    for get_point in get_dict:
        if message.startswith(get_point):
            if len(message) > 4:
                response = get_dict[get_point](message[3:])

    for item in dialog_dict:
        for text in item:
            if text in message:
                response = dialog_dict.get(item)

    if response is not None: return response
    return 'Извини, но я не могу ответить на это.'


dialog_dict = {
    ('прив', 'здрав'): 'Привет!',
    ('как дела', 'кд'): 'Хорошо!',
    ('тебя зовут', 'имя'): 'я ВК бот, меня зовут Аркадик!',
    ('пока', 'досвид', 'прощ'): 'Пока!'
}
command_dict = {
    'planet': get_planet,
    'starship': get_starship
}

get_dict = {
    '-g': get_games,
    '-w': get_info_wiki,
    '-c': get_course
}
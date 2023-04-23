import wikipedia


def get_info_wiki(article):
    wikipedia.set_lang('ru')
    try:
        return f'{wikipedia.summary(article)}'
    except wikipedia.WikipediaException:
        return 'Информация не найдена!'

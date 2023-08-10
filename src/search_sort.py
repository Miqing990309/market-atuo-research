from search import *


def search_sort(engine, keywords, time, district, number):
    result = []

    if engine == Engine.GOOGLE:
        result = search_by_google(keywords, time, district, number)
        return result
    elif engine == Engine.BING:
        return result
    elif engine == Engine.BAIDU:
        return result
    elif engine == Engine.YAHOO:
        return result
    elif engine == Engine.FIREFOX:
        return result

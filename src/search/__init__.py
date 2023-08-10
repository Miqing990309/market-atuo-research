from enum import Enum
from .google_search import search_by_google


class Engine(Enum):
    GOOGLE = 1
    BING = 2
    BAIDU = 3
    YAHOO = 4
    FIREFOX = 5

def search_by_google(query: str, time: str, district='', number=100):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'googlesearch' found")

    result = []
    print("Searching results in Google")
    for j in search(query, tld="com", tbs=time, country=district, num=number, stop=None, pause=2):
        result.append(j)

    return result

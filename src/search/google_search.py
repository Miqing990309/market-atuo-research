def searchByGoogle(query:str, time:str, district=''):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
    
    result = []
    for j in search(query, tld="com", tbs=time, country=district, num=10, stop=None, pause=2):
	    # print(j)
        result.append(j)

    return result

def main():
    query = "Geeksforgeeks"
    searchByGoogle(query)

if __name__ == '__main__':
    main()


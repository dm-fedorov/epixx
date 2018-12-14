# links.py
def get_url_count(url):
    '''
    Функция для подсчета гиперссылок в html-документе.
    '''
    import urllib.request
    import re
    try:
        with urllib.request.urlopen(url) as webpage:
            text = webpage.read().decode('utf-8')

        return len(re.findall(r'http(s)?://', text))

    except Exception as e:
        return e 

if __name__ == '__main__':
    url = 'https://pycode.ru/'
    print(get_url_count(url))

# tutchev_blank.py
def get_html(text, img):    
    '''
    Функция для генерации html-документа.
    '''
    import urllib.request
    try:
        # здесь код

    except Exception as error:
        print(error)        
    else:
        print("Файл создан!")

if __name__ == "__main__":
    get_html("http://dfedorov.spb.ru/python/files/tutchev.txt", "http://dfedorov.spb.ru/python/files/tutchev.jpg")   

    

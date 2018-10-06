# tutchev.py
import urllib.request

def get_html(text, img):    
    '''
    Функция для генерации html-документа.
    '''
    try:
        with open('file.html', 'w', encoding='utf-8') as f:
            f.write('''
            <!DOCTYPE html>
    <html>
        <head>
           <meta charset="utf-8">
           <title>Стихи</title>
        </head>
        <body>''')

            url = text
            with urllib.request.urlopen(url) as webpage:
                for line in webpage:
                    line = line.strip()
                    line = line.decode('utf-8')
                    f.write(line)
                    f.write("<br>")
              
            f.write('''
      <p><img src=''' + img + ''' alt="Тютчев"></p>
        </body>
    </html>''')

    except Exception as error:
        print(error)        
    else:
        print("Файл создан!")

if __name__ == "__main__":
    get_html("http://dfedorov.spb.ru/python/files/tutchev.txt", "http://dfedorov.spb.ru/python/files/tutchev.jpg")   

    

# file_write_with.py
def file_write(file):
    try:
        with open("top.txt", 'w') as output_file:
            count = output_file.write("Hello!\n")
        return count
    except:
        # как узнаем о состоянии ошибки
        return 0

if __name__ == '__main__':
    print('записано символов {0}'.format(file_write("top.txt")))

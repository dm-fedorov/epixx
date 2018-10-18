# file_reader.py
def file_reader(path):
    file = open(path, 'r')
    contents = file.read()
    file.close()

    return contents

if __name__ == '__main__':
    print(file_reader('example_text.txt'))

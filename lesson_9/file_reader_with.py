# file_reader_with.py
def read_file(file):
    try:
        with open(file, 'r') as file:
            contents = file.read()
    except:
        contents = None
    return contents

if __name__ == '__main__':
    print(read_file('example_text.txt'))



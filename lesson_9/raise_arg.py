# raise_arg.py
def check_arg(arg):
    if len(arg) < 3:
        # генерируем исключение, обрабатываем его вне функции:
        raise Exception('arg1 < 3')
    else:
        return len(arg)

if __name__ == '__main__':
    check_arg('3')

# format_module.py
def f(var1, var2):   
    '''
    Возвращает строку вида "var1 и var2"
    '''
    # проверяем версию Python для работы с f-строками
    import sys
    if sys.version_info[:2] >= (3, 6):
        return f'{var1} и {var2}'
    else:
        return '{0} и {1}'.format(var1, var2)

# raise_arg_try.py
def my_check_arg(arg):
    import raise_arg
    try:
        res = raise_arg.check_arg(arg)        
    except:
        res = None
    return res

if __name__ == '__main__':
    my_check_arg('3')
    

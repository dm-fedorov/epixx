# arg_list.py
def local_add_element(lst, element):
    import copy
    # создаем глубокую копию списка
    deepcopy_lst = copy.deepcopy(lst)
    deepcopy_lst.append(element)
    return deepcopy_lst

def global_add_element(element):
    lst.append(element)        

if __name__ == '__main__':
    lst = [4, 6]    
    print(local_add_element(lst, '5'))
    print(lst)
    global_add_element('5')
    print(lst)
    
    

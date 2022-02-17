'''
A program to move conveniently through .json object.
'''
import json


def get_data(path_to_file:str = 'info.json') -> dict:
    """
    Returns a dictionary which represents a .json object.
    Args:
        path_to_file (str): a path to json file to read.
    Returns:
        dict: a converted .json object.
    >>> type(get_data())
    <class 'dict'>
    """
    with open(path_to_file, mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def inspect_iterative(iterative) -> str:
    """
    Inspects iterative python object, showing a useful information to user.
    Args:
        iterative (dict or list): an iterative object.
    Returns:
        str: a set of indices if iterative is a list and a set of keys otherwise.
    >>> inspect_iterative([1, 2])
    ('This object is a list. Enter an index from 0 to 1:', True)
    """
    if isinstance(iterative, dict):
        keys = [str(key) for key in iterative.keys()]
        if len(keys) == 0:
            return 'This object is a dictionary of length 0.', False
        return 'This object is a dictionary. Enter one of it\'s keys:\n\t' + '\n\t'.join(keys), True
    elif isinstance(iterative, list):
        if len(iterative) == 0:
            return 'This object is a list of length 0.', False
        return f'This object is a list. Enter an index from 0 to {len(iterative) - 1}:', True
    else:
        return f'This object is not an iterative one. It\'s value is: {iterative}', False


def enter_inner_iterative(iterative, index):
    """
    Enters a iterative by the index or key.
    Args:
        iterative (list or dict): an iterative object - list or dict.
        index (int or subscripteble): an index or key.
    >>> enter_inner_iterative([1, 2, 3], 1)
    2
    """
    return iterative[index]


def proceed(iterative):
    """
    A recursive function which purpose is to navigate
    through the iterative type.
    Args:
        iterative (list or dictionary): an object to navigate through.
    """
    message, status = inspect_iterative(iterative)
    print(message)
    if status:
        print('>>> ', end='')
        idx = input()
        if idx == '..':
            return
    else:
        print('To return to the highest level, press Enter.')
        input('>>> ')
        return
    if isinstance(iterative, dict):
        try:
            inner = enter_inner_iterative(iterative, idx)
        except KeyError:
            print('The value you entered is invalid. Please, enter a correct one:')
            while True:
                try:
                    print('>>> ', end='')
                    idx = input()
                    inner = enter_inner_iterative(iterative, idx)
                    break
                except KeyError:
                    print('The value you entered is invalid. Please, enter a correct one:')
        proceed(inner)
    elif isinstance(iterative, list):
        try:
            idx = int(idx)
            inner = enter_inner_iterative(iterative, idx)
        except (ValueError, IndexError):
            print('The value you entered is invalid. Please, enter a correct one:')
            while True:
                try:
                    print('>>> ', end='')
                    idx = int(input())
                    inner = enter_inner_iterative(iterative, idx)
                    break
                except (ValueError, IndexError):
                    print('The value you entered is invalid. Please, enter a correct one:')
        proceed(inner)


def main():
    """
    The main function.
    """
    print('------------------------------------------------------------')
    print('|             To navigate through dictionary,              |')
    print('|             follow the messages in console.              |')
    print('|  If you want to return to the highest level, type "..".  |')
    print('------------------------------------------------------------')
    while True:
        print('You\'re on the hishest level.')
        proceed(get_data())


if __name__ == '__main__':
    main()

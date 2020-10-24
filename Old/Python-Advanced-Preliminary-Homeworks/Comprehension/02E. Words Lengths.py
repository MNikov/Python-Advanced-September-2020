def find_string_len():
    str_dict = {x: len(x) for x in input().split(', ')}
    return str_dict


def print_dict(dictionary):
    print(', '.join([f'{k} -> {v}' for k, v in dictionary.items()]))


print_dict(find_string_len())
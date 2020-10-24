def create_dict_with_chars_and_their_ascii_values():
    result_dict = {x: ord(x) for x in input().split(', ')}
    return result_dict


print(create_dict_with_chars_and_their_ascii_values())

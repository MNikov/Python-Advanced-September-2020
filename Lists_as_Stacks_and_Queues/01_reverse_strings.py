def reverse_string(string):
    reversed_list = []
    string_as_list = list(string)
    while string_as_list:
        reversed_list.append(string_as_list.pop())
    print(''.join(reversed_list))


reverse_string(input())

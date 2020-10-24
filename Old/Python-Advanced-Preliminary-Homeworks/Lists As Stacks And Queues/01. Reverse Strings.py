def string_reverse(string):
    reversed_list = []
    for char in string:
        reversed_list.append(char)
    while reversed_list:
        popped_char = reversed_list.pop()
        print(popped_char, end='')


string_reverse(input())
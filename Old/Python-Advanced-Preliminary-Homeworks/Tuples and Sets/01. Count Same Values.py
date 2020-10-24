def add_number(number_list):
    num_dict = {}
    for number in number_list:
        if number not in num_dict:
            num_dict[number] = 0
        num_dict[number] += 1
    return num_dict


def print_result(num_dict):
    for number, times in num_dict.items():
        print(f'{number} - {times} times')


print_result(add_number([float(i) for i in input().split()]))

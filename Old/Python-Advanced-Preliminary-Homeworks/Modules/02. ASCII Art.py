from pyfiglet import figlet_format


def print_message(string):
    print(figlet_format(string))


print_message(input())
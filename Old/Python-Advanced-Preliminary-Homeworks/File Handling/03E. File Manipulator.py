import os

while True:
    line = input()
    if line == 'End':
        break
    command, file_name, *args = line.split('-')
    if command == 'Create':
        file = open(file_name, 'w')
        file.close()
    elif command == 'Add':
        content = args[0]
        with open(file_name, 'a') as file:
            file.write(f'{content}\n')
    elif command == 'Replace':
        old_string, new_string = args
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                text = file.read()
            text = text.replace(old_string, new_string)

            with open(file_name, 'w') as file:
                file.write(text)
        else:
            print('An error occurred')
    elif command == 'Delete':
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print('An error occurred')

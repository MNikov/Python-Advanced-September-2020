import os

while True:
    line = input()
    if line == 'End':
        break
    tokens = line.split('-')
    command, file_name = tokens[0], tokens[1]
    if command == 'Create':
        new_file = open(file_name, 'w')
        new_file.close()
    elif command == 'Add':
        content = tokens[2]
        with open(file_name, 'a') as current_file:
            # no need for try-except block because the 'a' mode creates a file if it does not e
            current_file.write(content + '\n')
    elif command == 'Replace':
        old_string, new_string = tokens[2], tokens[3]
        try:
            with open(file_name) as current_file:
                text = current_file.read()
            text = text.replace(old_string, new_string)
            with open(file_name, 'w') as current_file:
                current_file.write(text)
        except FileNotFoundError:
            print("An error occurred")
    elif command == 'Delete':
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")

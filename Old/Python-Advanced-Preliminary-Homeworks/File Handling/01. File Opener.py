path = '.\\08-File-Handling-Lab-Resources\\File Opener\\text.txt'
try:
    file = open(path, 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')

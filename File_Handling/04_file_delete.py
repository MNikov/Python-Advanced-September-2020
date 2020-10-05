import os

path = 'my_first_file.txt'

if os.path.exists(path):
    os.remove(path)
else:
    print('File already deleted!')

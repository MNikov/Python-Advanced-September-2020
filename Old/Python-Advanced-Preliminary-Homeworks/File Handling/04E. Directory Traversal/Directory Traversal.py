import os

path = input()
sep_count = path.count(os.path.sep)
files_dict = {}

for root, dirs, files in os.walk(path):
    if sep_count - root.count(os.path.sep) > 1: # allows us to start from the 1st level of the directory given removing the previous /`s
        continue
    for file in files:
        extension = f".{file.split('.')[-1]}"  # -1 so that we can read files that have '.' in their names
        if extension not in files_dict:
            files_dict[extension] = []
        files_dict[extension].append(file)

result_str = ''
for ext, files in sorted(files_dict.items()):
    result_str += f'{ext}\n'
    for file in sorted(files):
        result_str += f'- - - {file}\n'

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
final_location = desktop + os.path.sep + 'report.txt'

with open(final_location, 'w') as file:
    file.write(result_str)

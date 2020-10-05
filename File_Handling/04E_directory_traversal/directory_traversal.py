import os

path = input()
files_dict = {}
sep_count = path.count(os.path.sep)

for root, directories, files in os.walk(path):
    if sep_count - root.count(os.path.sep) > 1:
        continue
    for file in files:
        file_extension = file.split('.')[-1]
        if file_extension not in files_dict:
            files_dict[file_extension] = []
        files_dict[file_extension].append(file)

result_string = ''
for ext, files in sorted(files_dict.items()):
    result_string += f'.{ext}\n'
    for file in sorted(files):
        result_string += f'- - - {file}\n'

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
final_path = desktop + os.path.sep + 'report.txt'

with open(final_path, 'w') as report_file:
    report_file.write(result_string)

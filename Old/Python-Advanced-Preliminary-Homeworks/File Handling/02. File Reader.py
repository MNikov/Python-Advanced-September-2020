path = '.\\08-File-Handling-Lab-Resources\\File Reader\\numbers.txt'
num_file = open(path, 'r')
num_sum = sum([int(x) for x in num_file])
print(num_sum)
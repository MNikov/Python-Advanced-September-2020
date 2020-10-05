path = '08-File-Handling-Lab-Resources\\File Reader\\numbers.txt'
num_file = open(path)
num_sum = sum([int(n) for n in num_file])
print(num_sum)
import fibonacci

while True:
    line = input()
    if line == 'Stop':
        break
    tokens = line.split()
    command = tokens[0]
    if command == 'Create':
        number = int(tokens[2])
        fibonacci.create_fib(number)
    elif command == 'Locate':
        number = int(tokens[1])
        fibonacci.locate(number)

from Modules.fibonacci_05 import fib_fn as fib

while True:
    line = input()
    if line == 'Stop':
        break
    tokens = line.split()
    if tokens[0] == 'Create':
        count = int(tokens[2])
        fib.create_sequence(count)
    else:
        number = int(tokens[1])
        fib.locate_number(number)

from collections import deque
from math import floor

expression = deque(input().split())
operators = ('+', '-', '*', '/')
numbers = deque()
# result = 0

while expression:
    char = expression.popleft()
    if char not in operators:
        numbers.append(int(char))
    else:
        result = 0
        if char == '+':
            while numbers:
                result += numbers.popleft()
        elif char == '-':
            result = numbers.popleft()
            while numbers:
                result -= numbers.popleft()
        elif char == '*':
            result = 1
            while numbers:
                result *= numbers.popleft()
        elif char == '/':
            result = numbers.popleft()
            while numbers:
                result /= numbers.popleft()
            result = floor(result)
        expression.appendleft(result)

print(result)


# # КОД ОТ УПРАЖНЕНИЕ
# from collections import deque
# from math import floor
#
# expression = deque(input().split())
# collected_numbers = []
#
# while True:
#     current_char = expression.popleft()
#     if current_char in ('+', '-', '*', '/'):
#         first_num = int(collected_numbers[0])
#
#         for number in collected_numbers[1:]:
#             if current_char == "-":
#                 first_num -= int(number)
#             elif current_char == "+":
#                 first_num += int(number)
#             elif current_char == "/":
#                 first_num /= int(number)
#             elif current_char == "*":
#                 first_num *= int(number)
#
#         expression.appendleft(str(floor(first_num)))
#         collected_numbers = []
#
#         if len(expression) == 1:
#             break
#     else:
#         collected_numbers.append(current_char)
#
# print(expression[0])
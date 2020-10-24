from math import log


def calc_log(num, base):
    if base == 'natural':
        print(f'{log(num):.2f}')
    else:
        print(f'{log(num, int(base)):.2f}')


calc_log(int(input()), input())


from sys import maxsize


def find_longest_intersection(number):
    max_len = -maxsize
    longest_intersection = set()
    for _ in range(number):
        range_1, range_2 = input().split('-')
        start_1, end_1 = [int(x) for x in range_1.split(',')]
        start_2, end_2 = [int(x) for x in range_2.split(',')]
        set_1 = set(x for x in range(start_1, end_1 + 1))
        set_2 = set(x for x in range(start_2, end_2 + 1))
        intersection = set_1.intersection(set_2)
        if len(intersection) > max_len:
            max_len = len(intersection)
            longest_intersection = intersection
    return longest_intersection


def print_result(set_result):
    print(f'Longest intersection is [{", ".join([str(x) for x in set_result])}] with length {len(set_result)}')


print_result(find_longest_intersection(int(input())))

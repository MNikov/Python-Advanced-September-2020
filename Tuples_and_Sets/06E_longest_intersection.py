from sys import maxsize


def find_longest_intersection(n: int):
    max_len = -maxsize
    best_intersection = set()
    for _ in range(n):
        first_pair, second_pair = input().split('-')
        first_start, first_end = [int(x) for x in first_pair.split(',')]
        second_start, second_end = [int(x) for x in second_pair.split(',')]
        range_one = set(range(first_start, first_end + 1))
        range_two = set(range(second_start, second_end + 1))
        current_intersection = range_one.intersection(range_two)
        if len(current_intersection) > max_len:
            max_len = len(current_intersection)
            best_intersection = current_intersection
    print(f"Longest intersection is {list(best_intersection)} with length {len(best_intersection)}")


find_longest_intersection(int(input()))

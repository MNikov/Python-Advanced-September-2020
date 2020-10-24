def flatten_list():
    num_groups = [x for x in input().split('|')]
    flattened_list = [num for num_group in num_groups[::-1] for num in num_group.split()]
    return flattened_list


print(' '.join(flatten_list()))

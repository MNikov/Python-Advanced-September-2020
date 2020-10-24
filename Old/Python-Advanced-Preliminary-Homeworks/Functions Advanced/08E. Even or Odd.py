def even_odd(*args):
    command = args[-1]
    nums = [int(x) for x in args if x not in ['even', 'odd']]
    if command == 'even':
        return [x for x in nums if x % 2 == 0]
    else:
        return [x for x in nums if x % 2 != 0]
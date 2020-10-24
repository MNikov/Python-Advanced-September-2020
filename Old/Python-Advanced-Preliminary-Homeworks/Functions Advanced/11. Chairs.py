def distribute_chairs(names, chairs, result=[]):
    if len(result) == chairs:
        print(', '.join(result))
        return
    for i, name in enumerate(names):
        result.append(name)
        distribute_chairs(names[i + 1:], chairs, result)
        result.pop()


names = input().split(', ')
chairs = int(input())
distribute_chairs(names, chairs)
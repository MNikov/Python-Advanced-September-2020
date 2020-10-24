def solve(clothes, rack_capacity):
    clothes_sum = 0
    racks_count = 1
    while clothes:
        current_sum = clothes.pop()
        clothes_sum += current_sum
        if clothes_sum == rack_capacity:
            if clothes:
                racks_count += 1
                clothes_sum = 0
        elif clothes_sum > rack_capacity:
            clothes.append(current_sum)
            clothes_sum -= current_sum
            racks_count += 1
            clothes_sum = 0
    print(racks_count)


clothes = [int(i) for i in input().split()]
rack_capacity = int(input())
solve(clothes, rack_capacity)

def count_racks(clothes, rack_capacity):
    clothes_sum = 0
    racks_count = 1
    while clothes:
        current_value = clothes.pop()
        clothes_sum += current_value
        if clothes_sum == rack_capacity:
            if clothes:
                racks_count += 1
                clothes_sum = 0
        elif clothes_sum > rack_capacity:
            clothes.append(current_value)
            clothes_sum -= current_value
            racks_count += 1
            clothes_sum = 0
    print(racks_count)


clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
count_racks(clothes, rack_capacity)

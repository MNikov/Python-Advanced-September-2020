def find_pos_num_sum(nums):
    pos_num_sum = 0
    for num in nums:
        if num > 0:
            pos_num_sum += num
    return pos_num_sum


def find_neg_num_sum(nums):
    neg_num_sum = 0
    for num in nums:
        if num < 0:
            neg_num_sum += num
    return neg_num_sum


def print_and_compare(pos_sum, neg_sum):
    print(neg_sum)
    print(pos_sum)
    if pos_sum > abs(neg_sum):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


nums = [int(x) for x in input().split()]
neg_sum = find_neg_num_sum(nums)
pos_sum = find_pos_num_sum(nums)
print_and_compare(pos_sum, neg_sum)

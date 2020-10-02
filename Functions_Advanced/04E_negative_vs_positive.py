nums = [int(x) for x in input().split()]
pos_sum = sum(filter(lambda x: x > 0, nums))
neg_sum = sum(filter(lambda x: x < 0, nums))

print(neg_sum)
print(pos_sum)
if pos_sum > abs(neg_sum):
    print("The positives are stronger than the negatives")
elif abs(neg_sum) > pos_sum:
    print("The negatives are stronger than the positives")

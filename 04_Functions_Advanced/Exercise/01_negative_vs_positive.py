def compare_numbers(*args):
    negatives_sum = sum([num for num in args if num < 0])
    positives_sum = sum([num for num in args if num > 0])
    print(negatives_sum)
    print(positives_sum)
    if abs(negatives_sum) > abs(positives_sum):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


nums = list(map(int, input().split()))  # no zeroes expected
compare_numbers(*nums)

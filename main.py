def find_all_factors(num):
    nums = []
    for i in range(1, num + 1):
        if num % i == 0:
            nums.append(i)
    return nums


num = int(input("Enter a number "))
print(find_all_factors(num))

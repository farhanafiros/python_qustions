
nums = [4, 8, 2, 6, 7]

first = nums.pop(0)
last = nums.pop(-1)

nums.insert(0, last)
nums.append(first)

print(nums)
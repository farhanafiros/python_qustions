#Today's Question: Find two numbers that have the smallest absolute difference.
nums = [4,9,6,1]
#out: [4,6]

smallest = abs(nums[0] - nums[1])
result = [nums[0], nums[1]]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):

        diff = abs(nums[i] - nums[j])

        if diff < smallest:
            smallest = diff
            result = [nums[i], nums[j]]

print(result)


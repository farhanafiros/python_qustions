nums =[5,8,3,9,2,10]
smallest=nums[0]
largest=nums[0]

for i in range(len(nums)):
    if nums[i] > largest:
        largest = nums[i]
    elif nums[i] < smallest:
        smallest = nums[i]

print(largest - smallest)
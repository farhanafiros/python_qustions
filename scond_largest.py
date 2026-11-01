nums =[5,8,3,9,2,10]
largest = nums[0]
for i  in nums:
    print(i,largest)
    if i > largest :
        largest = i

second = nums[5]
for i in nums:
        if i > second and i < largest:
            second = i
print(second)



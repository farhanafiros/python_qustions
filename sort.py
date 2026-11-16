#Today's Question: Sort an array without using built-in function.
nums =[4,9,6,1,2,0,1,8,5,3]
#out: [0,1,2,3,4,5,6,7,8,9]

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] > nums[j]:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i]= temp                 
print(nums)



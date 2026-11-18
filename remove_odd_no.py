#Question: Remove elements that appear an odd number of times
nums=[]
l=int(input("Enter the length:"))
for i in range(l):
    element=int(input("Enter the Element:"))
    nums.append(element)
print(nums)
count={}
result =[]
for i in nums:
    if i not in count:
        count[i] = 1
    else :
        count[i] += 1 
for i in nums:
    if count[i] % 2 == 0:
        
        result.append(i)

print(count)
print(result)
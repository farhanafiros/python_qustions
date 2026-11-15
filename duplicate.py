nums=[1,2,2,3,5,6,7,7]
duplicate=[]
unique =[]
for i in nums:
        if i not in duplicate:
            duplicate.append(i)
        else:
              unique.append(i)
print(unique)

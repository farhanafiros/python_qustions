#Ques: Check if all elements are unique.

inp=[4,6,2,8,9,9]
count = {}

result = True
for i in inp:
    if i in count:
        result = False
        break
    else:
        count[i] = 1
print(result)


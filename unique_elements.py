#Ques: Check if all elements are unique.

inp = [4,6,2,8,9]
count = {}


for i in inp:
    if i in count:
        print(False)
        break
    else:
        count[i] = 1
    print(True)
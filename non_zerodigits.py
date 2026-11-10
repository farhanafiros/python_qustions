#*Today's Question*:Move all zeros to the end of the list without changing the order of other elements.
lis = [0,0,0, 5, 0, 8, 3, 0, 7]
non_zero=[]
for i in lis:
    if i != 0:
        non_zero.append(i)
for i in lis:
    if i == 0:
        non_zero.append(i)
    
    
print(non_zero)

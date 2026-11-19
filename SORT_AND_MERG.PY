#Question: Merge two arrays into a single sorted arraAY
a = list(map(int,input("enter elements:").split()))
print(a)
b= list(map(int,input("enter elements:").split()))
print(b)

for i in a:
    b.append(i)


for i in range(len(b)):
    for j in range(i+1,(len(b))):
        if b[i] > b[j]:
            b[j],b[i]=b[i],b[j]                
print(b)
        
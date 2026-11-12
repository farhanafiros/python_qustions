#Today's question: Check if a given list contains only numbers.

lis = ["7", "5", "2", "8","sql"]

result = True

for i in lis:
    try:
        int(i)
    except ValueError:
        result = False
        

print(result)


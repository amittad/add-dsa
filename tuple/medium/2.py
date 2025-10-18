#Given a tuple of numbers, write a program to find the maximum and minimum elements.

tup=(11,3,4,22,67,9,1,65)
max=tup[0]
min=tup[0]
for i in tup:
    if max<i:
        max=i

    elif min>i:
        min=i    


print(max)  
print(min)      
#Write a Python program to remove duplicates from a tuple.
tup1=(1,2,1,3,4,2,5,6,4)
lenh=len(tup1)
tup2=()
for i in tup1:
    if i not in tup2:
        tup2+=(i,)


print(tup2)        

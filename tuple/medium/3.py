#Write a program to reverse a tuple without using slicing.
tup=(1,2,3,4,5,6,4,5,)
temp=()

for i in range(len(tup)-1, -1, -1,) :
    temp+=(tup[i],)

print(temp)    
print(tup[::-1])#slicing method

    

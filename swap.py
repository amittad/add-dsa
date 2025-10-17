array = [10, 20, 30,34,6,89,45,67]
small=array[0]
big=array[0]

smallest=[]
biggest=[]
for i in array:
    if i <small:
        small=i
        smallest.append(i)  
    elif i>big:
        big=i
        biggest.append(i)   


print("Smallest number is:",small)
print("Biggest number is:",big)   

print("All smallest numbers are:",smallest)
print("All biggest numbers are:",biggest)      
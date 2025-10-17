#Convert the tuple (1, 2, 3) into a list.
my_tuple = (1, 2, 3,5,6,7,7,7,8,9)
listtotuple=list(my_tuple)
for i in listtotuple:
    if i%2==0:
        for j in range(1,11):
            print(i*j)
        print("=================================")
    elif i%2!=0:
        for k in range(1,11):
            print(i*k)  
        print("=================================")          
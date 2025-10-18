#Convert a list of tuples like [(1, 2), (3, 4), (5, 6)] into two separate tuples: (1, 3, 5) and (2, 4, 6).

tuple1=[(1, 2), (3, 4), (5, 6)] 
tuple2=()
tuple3=()
for a,b in tuple1:
    tuple2+=(a,)
    tuple3+=(b,)


print(tuple2,tuple3)


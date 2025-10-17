a = [1, 2, 3, 56, 0, -1, 13, 99]

for x in a:
    if x > 0:
        for i in range(1, 11):
            print(x*i, end=' ')
    elif x == 0:
        print("Zero → no stars")
    else:
        print("-" * abs(x))  # negative numbers ke liye '-' print

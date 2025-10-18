elements = (1, 3, 5, 7, 8, 9, 34, 23, "amit")
inp = input("Enter an element to find in tuple: ")

found = False  # flag to track if element found or not

for i in elements:
    # Convert both to string for easy comparison (simple trick)
    if str(i) == inp:
        found = True
        break  # stop the loop if found

if found:
    print("Element found in tuple ✅")
else:
    print("Element not found ❌")

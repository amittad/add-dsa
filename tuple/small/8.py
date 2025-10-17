#‘apple’, ‘banana’, ‘cherry’, ‘banana’

fruits=("apple","banana","cherry")
fr=list(fruits)
for i in fr:
    if i=="apple":
        print(fr.index(i))
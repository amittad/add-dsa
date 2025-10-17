ch=int=(input("Enter a character: "))
for i in ch:    
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        print(i,"is a vowel")
    else:
        print(i,"is not a vowel")
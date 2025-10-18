#Given a tuple (1, 2, 3, 4, 5, 6), convert it into two tuples, each containing half the elements.

t1=(1,2,3,4,5,6,7,8,9,10)
t2=()
t3=()
length=len(t1)
h1=length//2
for i in range(h1):
    t2+=(t1[i],)

for i in range(h1,length):
    t3+=(t1[i],)    
print(t2) 
print(t3)   
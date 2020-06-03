n=int(input("enter the number of elements"))
l=[]
for i in range(n):
    l.append(int(input()))
def even(l):
    l1=[]
    for i in l:
        if(i%2==0):
            l1.append(i)
    l1.sort()
    return l1      
def odd(l):
    l2=[]
    for i in l:
        if(i%2!=0):
            l2.append(i)
    l2.sort()        
    return l2[::-1]
t=even(l)
print(t)
p=odd(l)
print(p)
print("new list is", p+t)

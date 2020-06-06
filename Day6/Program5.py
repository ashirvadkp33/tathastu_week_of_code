MAX = 100005
   
fibonacci = []
   
def createfib(): 
    f , s = 0, 1
    fibonacci.append(f) 
    fibonacci.append(s) 

    while (s <= MAX): 
        t = f + s 
        if t <= MAX: 
            fibonacci.append(t) 
        f = s 
        s = t 
   

def checkArray(l, n): 
    sum = 0
      
    for i in range(n): 
        if (l[i] in fibonacci): 
            sum += l[i] 
   
    if (sum in fibonacci): 
        return True
   
    return False
   
print("enter a list of integers: ",end="")
l = [int(x) for x in input().split()]
n = len(l) 
createfib() 
if (checkArray(l, n)): 
    print("Yes") 
else: 
    print("No") 

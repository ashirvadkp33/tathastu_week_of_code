def knapsack(W,wt,val,n):
    if n==0 or W==0:
        return 0

    if wt[n-1] > W :
        return knapsack(W,wt,val,n-1)
    
    else :
        return max(val[n-1]+ knapsack(W-wt[n-1],wt,val,n-1),knapsack(W, wt,val ,n-1))
    
val= list(map(int,input("Enter the element of val comma separatd : ").split(",")))
wt= list(map(int,input("Enter the element of list comma separatd : ").split(",")))
W = int(input("Enter the value of W: "))
n=len(val)
print(knapsack(W, wt, val, n))

def max_limit(List,n):
    if n == 0:
        return 0
    if n == 1:
        return List[0]
    val1= List[0]
    if n==2:
        return max(List)
    val2 = max(List[0],List[1])
    max_value = None
    
    for i in range(2,n):
        max_val=max(val1+List[i],val2)
        (val1,val2)=(val2,max_val)
    
    return max_val

my_items= list(map(int,input("Enter the element of list comma separatd : ").split(",")))
print(max_limit(my_items,len(my_items)))

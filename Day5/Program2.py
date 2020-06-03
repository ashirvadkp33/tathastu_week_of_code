def replace(lst):
    for i in range(len(lst)-1):
        lst[i]=max(lst[i+1:])
    return lst
my_list=list(map(int,input("Enter element of the list comma separated :").split(',')))
print("New List :",replace(my_list))

list1=[eval(x) for x in input("enter list1 elements seperated by comma").split(",")]
list2=[eval(x) for x in input("enter list2 elements seperated by comma").split(",")]  
print(list1,list2)
print("intersection of first and second list")
for i in list1:
    if i in list2:
        print(i)

k = int(input("enter the no. of lists you wanna enter: "))
l = []
for i in range(k):
    print("enter the sorted list: ")
    l.append([int(x) for x in input().split()])
    
final = []

final = list(l[0]) #copied first list in final

for i in range(1,k):
    f = 0 
    s = 0
    a = []
    while(f<len(final) or s<len(l[i])):
        if(final[f]<=l[i][s]):
            a.append(final[f])
            f+=1
        elif(final[f]>l[i][s]):
            a.append(l[i][s])
            s+=1
        if f==len(final):
            a.extend(l[i][s:len(l[i])])
            break
        elif s==len(l[i]):
            a.extend(final[f:len(final)])
            break
    final = list(a)        

print(final)

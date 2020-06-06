N = int(input("enter the dimension of square matrix: "))
l = []

for i in range(N):
    print("enter",N,"row elements:")
    l.append([int(x) for x in input().split()])

print("original matrix")

for i in range(0, N):    
        for j in range(0, N): 
            print(l[i][j],end = ' ') 
        print() 

for i in range(N//2): 
        for j in range(i, N-i-1): 
            temp = l[i][j] 
            l[i][j] = l[N-1-j][i] 
            l[N-1-j][i] = l[N-1-i][N-1-j] 
            l[N-1-i][N-1-j] = l[j][N-1-i] 
            l[j][N-1-i] = temp 

print("rotated matrix")

for i in range(0, N):    
        for j in range(0, N): 
            print(l[i][j],end = ' ') 
        print() 

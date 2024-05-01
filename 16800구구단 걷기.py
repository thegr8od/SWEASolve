data = [[] for _ in range(10)]
for i in range(1,10):
    for j in range(1,10):
        data[i].append(i*j)
    

t = int(input())
for tc in range(1,t+1):
    com = []
    n = int(input())
    min_val = 10**12
    for i in range(1,10):
        for j in range(9):
            if data[i][j] == n:
                com.append((i,j))
    for x,y in com:
        if (x-1) + (y-1) <= min_val:
            min_val = (x-1) + (y-1)
    print(min_val)  
                    
   
    
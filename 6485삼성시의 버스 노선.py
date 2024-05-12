t = int(input())

for tc in range(1,t+1):
    n = int(input())
    dic = {}
    for i in range(1,5001):
        dic[i] = 0
    data = []
    for i in range(n):
        start,end = map(int, input().split())
        for j in range(start,end+1):
            dic[j] += 1
            
    p = int(input())
    result = []
    
        
    for i in range(p):
        result.append(dic[int(input())])   
    print("#{} ".format(tc),end='')
    print(*result)
        
            
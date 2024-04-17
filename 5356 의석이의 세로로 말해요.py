t = int(input())

for tc in range(1,t+1):
    data = []
    for _ in range(5):
        data.append(list(input()))
    
    max_len = 0
    ans = []
    for i in data:
        if len(i) > max_len:
            max_len = len(i)
            
    for i in range(max_len):
        for j in range(5):
            if i < len(data[j]):
                ans.append(data[j][i])    
            
            
    print("#{} ".format(tc),end='')
    print(*ans,sep='')
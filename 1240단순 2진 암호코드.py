t = int(input())
key = [[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]

for tc in range(1,t+1):
    n,m = map(int, input().split())
    data = []
    for _ in range(n):
        data.append(list(map(int,input())))

    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                row = i
                last = j
    
    num = []
    for i in range(last-55,last,7):
        if data[row][i:i+7] in key:
            num.append(key.index(data[row][i:i+7]))
    
    odd = 0
    even = 0
    for i in range(len(num)):
        if i % 2 == 0:
            odd += num[i]
        else:
            even += num[i]
    ans = odd * 3 + even
    
    if ans % 10 == 0:
        print("#{} {}".format(tc,sum(num)))
    else:
        print("#{} 0".format(tc))        
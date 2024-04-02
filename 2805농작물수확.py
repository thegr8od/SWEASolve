t = int(input())

for q in range(t):
    n = int(input())

    farm = []
    cnt = 0

    for _ in range(n):
        farm.append(list(map(int, input())))

    for i in range(n//2+1):
        for j in range(n//2 - i, n//2 + i +1):
            cnt += farm[i][j]     

    for k in range(n//2-1,-1,-1):
        for l in range(n//2 -k, n//2 +k + 1):
            cnt += farm[n-k-1][l]
            
    print("#{} {}".format(q,cnt))
                    
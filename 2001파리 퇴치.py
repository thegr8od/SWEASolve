t = int(input())

for tc in range(1,t+1):
    n,m = map(int, input().split())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    
    ans = []
    i = 0
    j = 0
    while True:
        val = 0
        for a in range(i,m+i):
            for b in range(j,m+j):
                val += data[a][b]
        ans.append(val)
        i += 1
        if i == (n-m+1):
            i = 0
            j += 1
        if i == 0 and j ==( n-m+1):
            break
    print("#{} {}".format(tc,max(ans)))
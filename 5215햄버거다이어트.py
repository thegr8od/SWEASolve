t = int(input())

for tc in range(1,t+1):
    n,l = map(int, input().split())
    t = []
    k = []
    for _ in range(n):
        a,b = map(int,input().split())
        t.append(a)
        k.append(b)
    ans = 0
    def dfs(x,taste,kal):
        global ans
        if kal > l:
            return
        if taste >= ans:
            ans = taste
        if x == n:
            return
        
        dfs(x+1, taste+t[x], +kal+k[x])
        dfs(x+1,taste,kal)
        
    dfs(0,0,0)
    print("#{} {}".format(tc, ans))
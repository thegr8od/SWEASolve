t = int(input())

for tc in range(1,t+1):
    n,l = map(int, input().split())
    tlst = []
    klst = []
    for _ in range(n):
        t,k = map(int,input().split())
        tlst.append(t)
        klst.append(k)
        
    ans = 0
    
    def dfs(x,score,kal):
        global ans
        
        if kal > l:
            return
        if score >= ans:
            ans = score
        if x == n:
            return
        dfs(x+1, score + tlst[x], kal + klst[x])
        dfs(x+1, score, kal)
        
             

    
    dfs(0,0,0)
    print("#{} {}".format(tc,ans))            
                
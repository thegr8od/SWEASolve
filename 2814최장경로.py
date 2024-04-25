import sys
sys.setrecursionlimit(10**3)
t = int(input())

for tc in range(1,t+1):
    graph = []
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
        
    
    max_cnt = 0
    
    def dfs(x,cnt):
        global max_cnt
        if cnt > max_cnt:
            max_cnt = cnt
        visited[x] = True
        for i in graph[x]:
            if visited[i] == False:
                dfs(i,cnt+1)
        visited[x] = False
        return max_cnt
    
    for j in range(1,n+1):
        visited = [False for _ in range(n+1)]
        ans = dfs(j,1)
        
            
    print("#{} {}".format(tc, ans))    
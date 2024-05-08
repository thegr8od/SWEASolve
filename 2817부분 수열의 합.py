t = int(input())

for tc in range(1,t+1):
    n, k = map(int, input().split())
    graph = list(map(int, input().split()))
    visited = [False] * n
    cnt = 0
    def dfs(x,sum):
        global cnt
        if sum == k:
            cnt += 1
            return
        visited[x] = True
        for i in range(x,len(graph)):
            if visited[i] == False:
                dfs(i,sum+i)
        visited[x] = False
        
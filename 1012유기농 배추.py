#1012 유기농 배추(백준)
import sys
sys.setrecursionlimit(10**6)

t = int(input())
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for _ in range(t):
    m,n,k = map(int, input().split())
    visited = [[False] * m for _ in range(n)]
    graph = [[0]*m for _ in range(n)]
    for i in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1
    
    
    def dfs(x,y):
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    dfs(nx,ny)
        return True
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and graph[i][j] == 1:
                if dfs(i,j) == True:
                    cnt += 1
    print(cnt)
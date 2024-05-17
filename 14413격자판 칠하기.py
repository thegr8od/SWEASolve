t = int(input())

for tc in range(1,t+1):
    n,m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(input()))
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
        
    chk = 0
    def bfs(x,y):
        global chk
        val = graph[x][y]
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if 0 <= nx < n and 0<= ny <y:
                if val = '#':
                    graph[nx][ny] 
                
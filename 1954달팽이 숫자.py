t = int(input())

for tc in range(1,t+1):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    x,y = 0,0
    dist = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(1, n*n+1):
        graph[x][y] = i
        x += dx[dist]
        y += dy[dist]
        
        if x<0 or x>=n or y<0 or y>=n or graph[x][y] != 0:
            x -= dx[dist]
            y -= dy[dist]
            dist = (dist+1)%4
            x += dx[dist]
            y += dy[dist]
    
    print("#{}".format(tc))
    for row in graph:    
        print(*row)
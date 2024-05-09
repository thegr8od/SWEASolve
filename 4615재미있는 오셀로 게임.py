t = int(input())

for tc in range(1,t+1):
    n,m = map(int,input().split())
    board = [[0] * (n) for _ in range(n)]
    board[n//2 -1][n//2-1] = 2
    board[n//2 -1][n//2] = 1
    board[n//2][n//2-1] = 1
    board[n//2][n//2] = 2
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    
    for _ in range(m):
        x,y,c = map(int,input().split())
        for i in range(8):
            board[x-1][y-1] = c
            nx = x - 1 + dx[i]
            ny = y - 1 + dy[i]
            x_save = []
            y_save= []
            while 0 <= nx < n and 0 <= ny < n:
                x_save.append(nx)
                y_save.append(ny)
                if board[nx][ny] == 0:
                    break
                if board[nx][ny] == c:
                    for j in range(len(x_save)):
                        board[x_save[j]][y_save[j]] = c
                    break
                nx = nx + dx[i]
                ny = ny + dy[i]
    black = 0
    white = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    
    print("#{} {} {}".format(tc, black, white))
                    
            
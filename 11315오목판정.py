dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

t = int(input())
for tc in range(1,t+1):
    data = []
    n = int(input())
    for _ in range(n):
        data.append(list(input()))
    ans = 0
    for x in range(n):
        for y in range(n):
            if data[x][y] == 'o':
                for k in range(8):
                    nx = x +dx[k]
                    ny = y +dy[k]
                    cnt = 0
                    for _ in range(4):
                        if 0 <= nx < n and 0 <= ny < n:
                            if data[nx][ny] == 'o':
                                cnt += 1
                                if cnt == 4:
                                    ans += 1                         
                            nx += dx[k]
                            ny += dy[k]
    if ans == 0:
        print("#{} NO".format(tc))
    else:
        print("#{} YES".format(tc))

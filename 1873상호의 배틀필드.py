t = int(input())

for tc in range(1,t+1):
    h,w = map(int, input().split())
    data = []
    for _ in range(h):
        data.append(list(input()))

    x = 0
    y = 0
    for i in range(h):
        for j in range(w):
            if data[i][j] == '<' or data[i][j] =='^' or data[i][j] == 'v' or data[i][j] =='>':
               x, y = i,j
               
    n = int(input())
    cmd = list(input())
    curx = 0
    cury = 0
    for i in cmd:
        if i == 'U':
            if 0 <= x-1 < h and 0 <= y < w:
                if data[x-1][y] == '.':
                    data[x][y] = '.'
                    x = x-1
                    data[x][y] = '^'
                else:
                    data[x][y] = '^'
            else:
                data[x][y] = '^'
    
        elif i == 'D':
            if 0 <= x+1 < h and 0 <= y < w:
                if data[x+1][y] == '.':
                    data[x][y] = '.'
                    x = x+1
                    data[x][y] = 'v'
                else:
                    data[x][y] = 'v'    
            else:
                data[x][y] = 'v'
        elif i == 'L':
            if 0 <= x < h and 0 <= y-1 < w:
                if data[x][y-1] == '.':
                    data[x][y] = '.'
                    y = y-1
                    data[x][y] = '<'
                else:
                    data[x][y] = '<'    
            else:
                data[x][y] = '<' 
        elif i == 'R':
            if  0 <= x < h and 0 <= y+1 < w:  
                if data[x][y+1] == '.':
                    data[x][y] = '.'
                    y = y+1
                    data[x][y] = '>'
                else:
                    data[x][y] = '>'    
            else:
                data[x][y] = '>'
        elif i == 'S':
            if data[x][y] == '>':
                for j in range(y,w):
                    if data[x][j] == '#':
                        break
                    elif data[x][j] == '*':
                        data[x][j] = '.'
                        break
            elif data[x][y] == '<':
                for j in range(y,-1,-1):
                    if data[x][j] == '#':
                        break
                    elif data[x][j] == '*':
                        data[x][j] = '.'
                        break
            elif data[x][y] == '^':
                for j in range(x,-1,-1):
                    if data[j][y] == '#':
                        break
                    elif data[j][y] == '*':
                        data[j][y] = '.'
                        break
            elif data[x][y] == 'v':
                for j in range(x,h):
                    if data[j][y] == '#':
                        break
                    elif data[j][y] == '*':
                        data[j][y] = '.'
                        break 
    print("#{} ".format(tc),end='')
    for m in data:
        print("".join(m))
         
                        
                                                       
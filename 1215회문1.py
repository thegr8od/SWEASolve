for tc in range(1, 11):
    n = int(input())
    data = []
    for _ in range(8):
        data.append(list(input()))
    
    
    cnt = 0
    for i in range(8):
        for j in range(8):
            row = []
            column = []
            for k in range(n):
                if j+k < 8 :
                    row.append(data[i][j+k])
            for k in range(n):
                if i+k < 8:
                    column.append(data[i+k][j])
            if row == row[::-1] and len(row) == n:
                cnt += 1
            if column == column[::-1] and len(column) == n:
                cnt += 1       
                    
    
    print("#{} {}".format(tc, cnt))
                       
        
for tc in range(1, 11):
    n = int(input())
    data = []
    for _ in range(100):
        data.append(list(input()))
    
    
    stand = 0
    for i in range(100):
        for j in range(100):
            row = []
            column = []
            for k in range(100):
                if j+k < 100 :
                    row.append(data[i][j+k])
                    if row == row[::-1]:
                        if len(row) >= stand:
                            stand = len(row)
            for k in range(100):
                if i+k < 100:
                    column.append(data[i+k][j])
                    if column == column[::-1]:
                        if len(column) >= stand:
                            stand = len(column)       
                    
    
    print("#{} {}".format(n, stand))
                       
        
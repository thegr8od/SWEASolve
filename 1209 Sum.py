for tc in range(1,11):
    t = int(input())
    data = []
    for _ in range(100):
        data.append(list(map(int, input().split())))
    
    row_val = 0
    column_val = 0
    rightdiag_val = 0
    leftdiag_val = 0
    
    for i in range(100):
        row_val2 = 0
        for j in range(100):
            row_val2 += data[i][j]
        if row_val2 >= row_val:
            row_val = row_val2 
    
    for j in range(100):
        column_val2= 0
        for i in range(100):
            column_val2 += data[i][j]        
        if  column_val2 >= column_val:
            column_val = column_val2
            
    for k in range(100):
        rightdiag_val += data[k][k]
        
    for k in range(99,-1,-1):
        leftdiag_val += data[k][k] 
   
    print("#{} {}".format(tc,max(row_val, column_val, rightdiag_val, leftdiag_val)))

        
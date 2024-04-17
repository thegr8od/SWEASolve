t = int(input())

for tc in range(1, t+1):
    data = []
    data = list(input())
    cnt = 0
    for i in data:
        if i == 'x':
            cnt += 1
            
    if cnt >= 8:
        cnt = 'NO'
    else:
        cnt = 'YES'
    
    print("#{} {}".format(tc, cnt))
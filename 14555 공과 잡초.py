t = int(input())

for tc in range(1,t+1):
    data = list(input())
    cnt = 0
    for i in data:
        if i == '(' or i == ')':
            cnt += 1
    for j in range(len(data)-1):
        if data[j] == '(' and data[j+1] == ')':
            cnt -=1
            
    print("#{} {}".format(tc, cnt))
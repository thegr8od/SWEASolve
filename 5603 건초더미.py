t = int(input())
for tc in range(1,t+1):
    data =[]
    sum = 0
    n = int(input())
    for i in range(n):
        value = int(input())
        sum += value
        data.append(value)
    sum = sum // n
    cnt = 0
    for j in data:
        if j > sum:
           cnt += (j - sum)
    
    print("#{} {}".format(tc, cnt)) 
            
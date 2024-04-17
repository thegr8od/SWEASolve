t = int(input())

for tc in range(1,t+1):
    n = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    for i in range(1,n-1):
        if data[i] != max(data[i-1],data[i],data[i+1]) and data[i] != min(data[i-1],data[i],data[i+1]):
            cnt += 1
            
    print("#{} {}".format(tc, cnt)) 
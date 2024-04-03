t = int(input())

for i in range(t):
    n = int(input())
    data = list(map(int,input().split()))
    cnt = 0
    mid = sum(data) / n
    for j in data:
        if j <= mid:
            cnt += 1
    print("#{} {}".format(i+1, cnt))
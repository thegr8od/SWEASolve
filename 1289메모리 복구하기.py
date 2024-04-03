t = int(input())

for i in range(t):
    num = list(map(int, input()))
    start = [0] * len(num)
    cnt = 0
    for j in range(len(num)):
        if start[j] != num[j]:
            start[j:] = [num[j]] * len(start[j:])
            cnt += 1
    
    print("#{} {}".format(i+1, cnt))
            
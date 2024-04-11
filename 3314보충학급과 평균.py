t = int(input())

for tc in range(1, t+1):
    data = list(map(int, input().split()))
    sum = 0
    for i in data:
        if i >= 40:
            sum += i
        else:
            sum += 40
    print("#{} {}".format(tc, sum // 5))
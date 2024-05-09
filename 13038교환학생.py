t = int(input())
for tc in range(1, t+1):
    n = int(input())
    data = list(map(int, input().split()))
    one = data.count(1)
    lst = []
    for i in range(len(data)):
        if data[i] == 1:
            lst.append(i)
    while cnt == n:
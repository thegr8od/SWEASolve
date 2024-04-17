t = int(input())

data = [ _ for _ in range(12)]

for i in range(1,13):
    if i == 2:
        data[i-1] = [0 for _ in range(29)]
    elif i in [4,6,9,11]:
        data[i-1] = [0 for _ in range(30)]
    else:
        data[i-1] = [0 for _ in range(31)]

day = 4

for i in range(12):
    for j in range(len(data[i])):
        data[i][j] = day % 7
        day += 1

for tc in range(1, t+1):
    m, d = map(int, input().split())
    print("#{} {}".format(tc, data[m-1][d-1]))

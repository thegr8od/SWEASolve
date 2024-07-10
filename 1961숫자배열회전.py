tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    # 90도
    rotate90 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotate90[j][n-1-i] = data[i][j]

    # 180도
    rotate180 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotate180[n-1-i][n-1-j] = data[i][j]

    # 270도
    rotate270 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotate270[n-1-j][i] = data[i][j]

    print("#{}".format(t))
    for i in range(n):
        print("{} {} {}".format(
            "".join(map(str, rotate90[i])),
            "".join(map(str, rotate180[i])),
            "".join(map(str, rotate270[i]))
        ))
tc = int(input())
for t in range(1,tc+1):
    data = []
    n, m = map(int, input().split())
    
    for _ in range(n):
        data.append(list(map(int, input().split())))

    ans = 0

    for i in range(n):
        for j in range(n):
            plus = data[i][j]
            x = data[i][j]

            for k in range(1, m):
                if i + k < n:
                    plus += data[i + k][j]
                if i - k >= 0:
                    plus += data[i - k][j]
                if j + k < n:
                    plus += data[i][j + k]
                if j - k >= 0:
                    plus += data[i][j - k]

                if i + k < n and j + k < n:
                    x += data[i + k][j + k]
                if i + k < n and j - k >= 0:
                    x += data[i + k][j - k]
                if i - k >= 0 and j + k < n:
                    x += data[i - k][j + k]
                if i - k >= 0 and j - k >= 0:
                    x += data[i - k][j - k]

            ans = max(ans, plus, x)

    print("#{} {}".format(t,ans))

tc = int(input())

for t in range(1, tc + 1):
    n, m = map(int, input().split())
    ans = 0
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    if n > m:
        # a>b
        for i in range(n - m + 1):
            cur = 0
            for j in range(m):
                cur += a[i + j] * b[j]
            if cur > ans:
                ans = cur
    else:
        # b<a
        for i in range(m - n + 1):
            cur = 0
            for j in range(n):
                cur += b[i + j] * a[j]
            if cur > ans:
                ans = cur

    print("#{} {}".format(t, ans))

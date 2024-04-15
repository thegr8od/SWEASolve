t = int(input())

for tc in range(1,t+1):
    n = int(input())
    ans = 0
    for i in range(n):
        p, x = map(float, input().split())
        ans += p * x
    print("#{} {:.6f}".format(tc, ans))
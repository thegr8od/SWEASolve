t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    ans = a+b
    if ans >= 24:
        ans -= 24
    print("#{} {}".format(i+1, ans))

t = int(input())

for tc in range(1,t+1):
    a,b,c = map(int, input().split())
    ans = 0
    if a == b :
        ans = c
    elif a == c:
        ans = b
    elif b == c:
        ans = a
    print("#{} {}".format(tc, ans))
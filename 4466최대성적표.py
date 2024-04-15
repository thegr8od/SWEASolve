t = int(input())
for tc in range(1, t+1):
    n,k = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    ans = 0
    for i in range(k):
        ans += data[i]
    print("#{} {}".format(tc, ans))
        
t = int(input())

for tc in range(1,t+1):
    d,h,m = map(int, input().split())
    date = (d-11) * 1440
    hour = (h-11) * 60
    minute = m-11
    ans = date+ hour +minute
    if ans < 0:
        ans = -1
    print("#{} {}".format(tc,ans))
    
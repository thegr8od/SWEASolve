#20728 공평한 분배
t = int(input())

for tc in range(1,t+1):
    n,k = map(int, input().split())
    data = list(map(int,input().split()))
    data.sort(reverse=True)
    ans = 10**9 +1
    for i in range(n-k+1):
        diff = data[i] - data[i+k-1]
        ans = min(ans, diff)
            
    print("#{} {}".format(tc,ans))
        
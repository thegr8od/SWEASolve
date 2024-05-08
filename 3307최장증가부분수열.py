t = int(input())
for tc in range(1,t+1):
    n =int(input())
    
    data =list(map(int, input().split()))
    
    dp = [1 for i in range(n)]
    
    for i in range(n):
        for j in range(i):
            if data[i] > data[j]:
                dp[i] = max(dp[i], dp[j]+1)
    
    print("#{} {}".format(tc, max(dp)))
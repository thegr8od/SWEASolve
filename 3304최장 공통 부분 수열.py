t = int(input())

for tc in range(1,t+1):
    a,b = input().split()
    dp = [[0] * (len(a) + 1) for _ in range(len(b) +1)]

    for i in range(1,len(dp)):
        for j in range(1, len(dp[i])) :
            if a[j-1] == b[i-1] :
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    print("#{} {}".format(tc, dp[len(a)-1][-1]))            
        
        
        
        
    
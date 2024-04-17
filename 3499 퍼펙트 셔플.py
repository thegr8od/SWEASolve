t = int(input())


for tc in range(1,t+1):
    top = []
    bot = []
    ans = []
    n = int(input())
    data = list(input().split())
    if n % 2 == 0:
        ran = n // 2
    else:
        ran = n//2 +1
    for i in range(ran):
        top.append(data[i])
    
    for j in range(ran,n):
        bot.append(data[j])
    
    for k in range(ran):
        ans.append(top[k])
        if k < n//2:
            ans.append(bot[k])
    
    print("#{} ".format(tc),end='')    
    print(*ans, sep=' ')
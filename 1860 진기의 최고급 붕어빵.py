t = int(input())

for tc in range(1,t+1):
    n,m,k = map(int, input().split())
    # n = 사람 , m =걸리는 초, k = m시간 붕어빵
    data = list(map(int, input().split()))
    data.sort()
    ans = 0
    bread= 0
    if data[0] < m:
        ans = 1
    idx = 0
    for i in data:
        idx += 1
        check = (i // m) * k - idx
        if ((i // m) * k - idx) >= 0:
            continue
        else:
            ans += 1
    
    if ans == 0:
        print("#{} Possible".format(tc))
    else:
        print("#{} Impossible".format(tc))
            
        
        
        
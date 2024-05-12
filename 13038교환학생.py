t = int(input())
for tc in range(1, t+1):
    n = int(input())
    data = list(map(int, input().split()))
    start = []
    ans = []
    for i in range(len(data)):
        val = 0
        cnt = 0
        while val != n:
            if data[i] == 1:
                val += 1
            cnt += 1
            i += 1
            if i == 7:
                i = 0
        ans.append(cnt)
        
    print("#{} {}".format(tc,min(ans)))
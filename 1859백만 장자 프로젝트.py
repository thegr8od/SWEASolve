#1859백만 장자 프로젝트
t = int(input())

for tc in range(1,t+1):
    n = int(input())
    data = list(map(int, input().split()))
    max = data[-1]
    ans = 0
    for i in range(n-1,-1,-1):
        if data[i] > max:
            max = data[i]
        else:
           ans += (max - data[i])
    print("#{} {}".format(tc,ans)) 
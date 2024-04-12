t = int(input())

for tc in range(1,t+1):
    n , l = map(int, input().split())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    
    ans = 0
    for j in range(n):
        now = data[j][1]
        for k in range(n):
           if data[j][1] + data[k][1] <=      
t = int(input())

for tc in range(1,t+1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    cnt  =0    
    for i in range(n):
        for j in range(n):
            if data[i][0] > data[j][0] and data[i][1] < data[j][1]:
                cnt +=1
            if data[i][0] < data[j][0] and data[i][1] > data[j][1]:
                cnt +=1
                
    print("#{} {}".format(tc, cnt//2))        
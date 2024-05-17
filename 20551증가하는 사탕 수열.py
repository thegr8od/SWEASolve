t = int(input())

for tc in range(1,t+1):
    data = list(map(int, input().split()))
    cnt =0
    while data[1] >= data[2]:
        data[1] -=1
        cnt += 1
    while data[0] >= data[1]:
        data[0] -=1
        cnt +=1
    
    if data[0] == 0 or data[1] == 0 or data[2] == 0:
        print("#{} -1".format(tc))
    else:
        print("#{} {}".format(tc,cnt))
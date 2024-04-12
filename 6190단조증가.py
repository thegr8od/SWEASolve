t = int(input())
for tc in range(1, t+1):
    n = int(input())
    data = list(map(int,input().split()))
    max_value = -1
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            value = data[i] * data[j]
            if value <= max_value:
                continue
            now_value = list(map(int, str(value)))
            check = 0
            for k in range(len(now_value)-1):
                if now_value[k] > now_value[k+1]:
                    check = -1
            if check != -1 and value >= max_value:
                max_value = value
                
        
    print("#{} {}".format(tc,max_value))
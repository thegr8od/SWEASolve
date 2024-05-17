#20934 방울 마술
t = int(input())

for tc in range(1,t+1):
    data,n = input().split()
    data = list(data)
    n = int(n)
    
    while n:
        for i in range(len(data)):
            if data[i] == 'o' and i == 0:
                data[i], data[i+1] = data[i+1], data[i]
                n -= 1
                break
            elif data[i] == 'o' and i ==1:
                data[i], data[i-1] = data[i-1], data[i]
                n -= 1
                break
            elif data[i] == 'o' and i == 2:
                data[i], data[i-1] = data[i-1], data[i]
                n -= 1
                break
    print("#{} {}".format(tc,data.index('o')))            
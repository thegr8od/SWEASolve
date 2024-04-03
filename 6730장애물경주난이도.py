t = int(input())
for i in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    
    upp = 0
    low = 0
    
    for j in range(n-1):
        if data[j] <= data[j+1]:
            val = data[j+1] - data[j]
            if val >= upp:
                upp = val
        elif data[j] >= data[j+1]:
            val = data[j] - data[j+1]
            if val >=low:
                low = val
    
    print("#{} {} {}".format(i+1, upp, low))
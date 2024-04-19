data = [0] * 1000
t = int(input())
print(data[0])
for tc in range(1, t+1):
    p,q = map(int, input().split())
    
    for i in range(1,1000):
        data[i] = data[i-1] + i
    print(data[1])
    print(data[2])    
    print(data[4])
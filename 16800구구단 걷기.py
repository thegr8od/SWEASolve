t = int(input())

for tc in range(1, t+1):
    
    n = int(input())
    data = []
    
    for i in range(1, int(n ** 0.5) + 1):
        if n% i == 0:
            data.append((i-1) + (n // i) -1)
            
    print('#{} {}'.format(tc,min(data)))
    
t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    cnt = 0
    for j in range(a,b+1):
        c = j ** (1/2)
        if c == int(c):
            j = str(j)
            c = str(int(c))
            if j == j[::-1] and c == c[::-1]:
                cnt += 1
    
    print("#{} {}".format(i+1, cnt))
        
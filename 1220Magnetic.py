for i in range(1,11):
    n = int(input())
    data = []
    for j in range(n):
        data.append(list(map(int,input().split())))
        
    cnt = 0
    for k in range(n):
        r, c = 0, k
        stack = []
        while r < n:
            if not stack and data[r][c] == 1:
                stack.append(1)
            elif stack and data[r][c] == 2:
                cnt += stack.pop()
            r += 1
    
    print("#{} {}".format(i, cnt))
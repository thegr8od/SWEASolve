from collections import deque

for tc in range(1,11):
    n = int(input())
    queue = list(map(int, input().split()))
    queue = deque(queue)
    
    while True:
        for i in range(1,6):
            idx = queue.popleft() - i
            if idx <= 0:
                idx = 0
                queue.append(idx)
                break
            else:
                queue.append(idx)
        if idx == 0:
            break
    print("#{} ".format(n),end="")        
    print(*queue)
    
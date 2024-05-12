from collections import deque

t = int(input())

for tc in range(1,t+1):
    n,m = map(int, input().split())
    r = []
    w = []
    inout = []
    for _ in range(n):
        r.append(int(input()))
    for _ in range(m):
        w.append(int(input()))
    for _ in range(m*2):
        inout.append(int(input()))
    idx = 0
    earn = 0
    wait = []
    state = [0] * n
    while inout:
        if wait:
            for i in range(n):
                if state[i] == 0:
                    state[i] = wait.pop(0)
        
        car_num = inout.pop(0)
        if car_num > 0:
            for i in range(n):
                if state[i] == 0:
                    state[i] = car_num
                    break
            else:
                wait.append(car_num)
        else:
            car_num = abs(car_num)
            park_num = 0
            for i in range(n):
                if state[i] == car_num:
                    park_num = i
                    state[i] = 0
                    earn += (w[car_num-1] * r[park_num])
                    break
                
    print("#{} {}".format(tc, earn))
                
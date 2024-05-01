t = int(input())

for tc in range(1,t+1):
    data = list(input().split())
    n = int(data[0])
    cmd = data[1:]
    cur = [1,1]
    b = []
    o = []
    for i in range(1,len(data),2):
        if data[i] == 'B':
            b.append(int(data[i+1]))
        else:
            o.append(int(data[i+1]))
    time = 0
    while cmd:
        if cmd[0] == 'B':
            if cur[0] < int(cmd[1]):
                cur[0] +=1
            elif cur[0] > int(cmd[1]):
                cur[0] -=1
            elif cur[0] == int(cmd[1]):
                cmd.pop(0)
                cmd.pop(0)
                b.pop(0)
        
            if len(o) != 0:
                if cur[1] < o[0]:
                    cur[1] += 1
                elif cur[1] > o[0]:
                    cur[1] -= 1
                else:
                    pass
        elif cmd[0] == 'O':
            if cur[1] < int(cmd[1]):
                cur[1] +=1
            elif cur[1] > int(cmd[1]):
                cur[1] -=1
            elif cur[1] == int(cmd[1]):
                cmd.pop(0)
                cmd.pop(0)
                o.pop(0)    
                
            if len(b) != 0:
                if cur[0] < b[0]:
                    cur[0] += 1
                elif cur[0] > b[0]:
                    cur[0] -= 1
                else:
                    pass  
        time += 1      
    print("#{} {}".format(tc,time))      
    
        
        
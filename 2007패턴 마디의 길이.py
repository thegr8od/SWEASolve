t = int(input())

for tc in range(1,t+1):
    cmd = input()
    idx = 0
    for i in range(1,11):
        cmd1 = cmd[0:i]
        cmd2 = cmd[i:i*2]
        if cmd1 == cmd2:
           idx = len(cmd1)
           break 
    print("#{} {}".format(tc,idx))       
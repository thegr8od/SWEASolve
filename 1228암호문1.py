for tc in range(1,11):
    n = int(input())
    data = list(map(int, input().split()))
    cmd_n = int(input())
    cmd = list(input().split())
    for i in range(len(cmd)):
        if cmd[i] == 'I':
            x = int(cmd[i+1])
            y = int(cmd[i+2])
            s = []
            for j in range(y):
                s.append(cmd[i+3+j])
            for k in range(len(s)):
                data.insert(x+k,int(s[k])) 
                
    ans = data[:10]
    print("#{} ".format(tc),end='')
    print(*ans, sep=' ')   
    
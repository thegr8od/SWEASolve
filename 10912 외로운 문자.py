t = int(input())
for tc in range(1,t+1):
    data = list(input())
    stack = []
    for i in range(len(data)):
        if not data[i] in stack:
            stack.append(data[i])
        else:
            stack.remove(data[i])
    
    stack.sort()
    print("#{} ".format(tc),end='')
    if len(stack) == 0:
        print('Good')
    else:
        print(*stack,sep='')     
        
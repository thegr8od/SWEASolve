for tc in range(1,11):
    n,number = map(int, input().split())
    data = list(map(int, str(number)))
    stack = []
    for i in data:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
                
    ans = ''.join(map(str,stack))
    print("#{} {}".format(tc, int(ans)))
        
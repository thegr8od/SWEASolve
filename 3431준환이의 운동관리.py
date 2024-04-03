t = int(input())

for i in range(t):
    l,u,x = map(int, input().split())
    ans = 0
    if x <= l:
        ans = l - x
    elif x > l and x <= u:
        ans = 0
    else:
        ans = -1
        
    print("#{} {}".format(i+1,ans))
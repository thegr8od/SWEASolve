t = int(input())

for i in range(t):
    a,b = map(int, input().split())
    if a <= 9 and b <= 9:
        ans = a * b
    else:
        ans = -1
    
    print("#{} {}".format(i+1, ans))
    
    
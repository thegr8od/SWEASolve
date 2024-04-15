t =int(input())

for tc in range(1,t+1):
    n,d = map(int,input().split())
    range = d *2 + 1
    
    if n % range == 0:
        ans = n // range
    else:
        ans = (n // range) + 1

    print("#{} {}".format(tc, ans))
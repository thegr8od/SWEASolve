t = int(input())

for tc in range(1,t+1):
    n,a,b = map(int, input().split())
    min_val = a + b - n
    if min_val <= 0:
        min_val = 0
    max_val = min(a,b)
    print("#{} {} {}".format(tc,max_val,min_val))
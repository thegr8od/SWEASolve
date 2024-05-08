t = int(input())

for tc in range(1,t+1):
    d,a,b,f = map(int,input().split())
    time = d / (a+b)
    print("#{} {:.10f}".format(tc, time*f))
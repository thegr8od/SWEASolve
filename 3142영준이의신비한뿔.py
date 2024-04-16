t = int(input())

for tc in range(1,t+1):
    n,m = map(int,input().split())
    two_horn = n - m
    print("#{} {} {}".format(tc, m-two_horn, two_horn))
        
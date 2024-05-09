import math

t = int(input())

for tc in range(1, t+1):
    n,r = map(int,input().split())
    print("#{} {}".format(tc,math.comb(n,r)%1234567891))
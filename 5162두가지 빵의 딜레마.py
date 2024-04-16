t = int(input())

for tc in range(1,t+1):
    a, b, c = map(int, input().split())
    value = min(a,b)
    print("#{} {}".format(tc, c // value))
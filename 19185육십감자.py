#육십감자
t = int(input())

for tc in range(1,t+1):
    n,m = map(int, input().split())
    data1 = list(input().split())
    data2 = list(input().split())
    q = int(input())
    ans = []
    for _ in range(q):
        y = int(input())
        data1_idx = y % n -1
        data2_idx = y % m -1
        ans.append(data1[data1_idx]+data2[data2_idx])
    print("#{} ".format(tc),end='')
    print(*ans)
t = int(input())

for tc in range(1,t+1):
    n,k = map(int, input().split())
    data = list(map(int, input().split()))
    people = [i for i in range(1,n+1)]
    ans = []
    for j in people:
        if j not in data:
            ans.append(j)

    print("#{} ".format(tc), end="")
    print(*ans, sep=" ")
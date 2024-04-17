t = int(input())

for tc in range(1,t+1):
    data = list(input())
    h = int(input())
    idx = list(map(int, input().split()))
    idx.sort(reverse=True)
    for i in idx:
        data.insert(i, '-')
    
    print("#{} ".format(tc),end='')
    print(*data,sep='')
t = int(input())

for tc in range(1,t+1):
    n,m = map(int,input().split())
    if m == 0:
         print('#{} OFF'.format(tc))
    else:
        data =[]
        for i in range(n):
            idx = (m % 2)
            m = m // 2
            if idx != 1:
                print('#{} OFF'.format(tc))
                break
        else:
             print('#{} ON'.format(tc))
            
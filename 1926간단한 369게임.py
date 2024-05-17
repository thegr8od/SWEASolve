#369 게임
n = int(input())

for i in range(1,n+1):
    chk = list(str(i))
    cnt = 0
    for j in range(len(chk)):
        if chk[j] == '3' or chk[j] == '6' or chk[j] == '9':
            chk[j] = '-'
            cnt += 1
            
    if '-' in chk:
        print('-'*cnt, end=' ')
    else:
        print(*chk, end=' ', sep='')
        

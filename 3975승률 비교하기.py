data = []
t = int(input())

for tc in range(1,t+1):
    data.append(list(map(int, input().split())))
    
for tc in range(1,t+1):
    a,b,c,d = data[tc-1][0], data[tc-1][1], data[tc-1][2], data[tc-1][3]
    alice = a /b
    bob = c/d
    
    if alice > bob:
        print("#{} ALICE".format(tc))
    elif bob > alice:
        print("#{} BOB".format(tc))
    else:
        print("#{} DRAW".format(tc))

t = int(input())

S = []
D = []
H = []
C = []

for tc in range(1,t+1):
    data = list(input())
    for i in range(4):
        idx = 0 + (3*i)
        if data[idx] == 'S':
            S.append("".join(data[idx+1]+data[idx+2]))
    print(S)
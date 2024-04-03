t = int(input())

for i in range(1,t+1):
    a,b = 1,1
    vec = list(input())
    for j in vec:
        if j == 'L':
            b = a+b
        else:
            a = a+b
    print("#{} {} {}".format(i, a, b))
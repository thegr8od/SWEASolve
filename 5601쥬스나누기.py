t = int(input())

for i in range(1,t+1):
    n = int(input())
    print("#{}".format(i),end="")
    for j in range(n):
        print(" {}{}{}".format(1,"/",n),end="")
    print()
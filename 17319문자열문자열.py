t = int(input())

for tc in range(1,t+1):
    n = int(input())
    data = list(input())
    data1 = data[0:n//2]
    data2 = data[n//2:n]
    if data1 == data2:
        print("Yes")
    else:
        print("no")
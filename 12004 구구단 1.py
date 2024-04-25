t = int(input())

data = set()
for i in range(1,10):
    for j in range(1,10):
        data.add(i*j)

data = list(data)
for tc in range(1,t+1):
    n = int(input())
    if n in data:
        print("#{} Yes".format(tc))
    else:
        print("#{} No".format(tc))
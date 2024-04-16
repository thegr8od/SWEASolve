t = int(input())
lst = [0] * 64
for tc in range(1,t+1):
    data = list(input())
    check = 0
    for i in data:
        if data.count(i) != 2:
            check += 1
    
    if check == 0:
        print("#{} Yes".format(tc))
    else:
        print("#{} No".format(tc))
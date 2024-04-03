t = int(input())

for i in range(1,t+1):
    n = int(input())
    right_ans = list(input())
    wrong_ans = list(input())
    cnt = 0
    for j in range(n):
        if right_ans[j] == wrong_ans[j]:
            cnt +=1
    print("#{} {}".format(i,cnt))
t = int(input())

for tc in range(1,t+1):
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    data_sum = []
    for i in range(7):
        for j in range(i+1,7):
            for k in range(j+1,7):
                sum = data[i] + data[j] + data[k]
                data_sum.append(sum)
    data_sum = set(data_sum)
    data_sum = sorted(list(data_sum), reverse=True)
    print("#{} {}".format(tc,data_sum[4]))
    
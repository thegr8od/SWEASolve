t = int(input())
for tc in range(1,t+1):
    data = list(map(int, input().split()))
    sum_data = 0
    for i in data:
        sum_data += i
    
    sum_data -= (min(data)+max(data))
    sum_data = sum_data / (len(data) -2)
    print("#{} {:.0f}".format(tc,sum_data))
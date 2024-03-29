
for i in range(1,11):
    t = int(input())
    lst = list(map(int, input().split()))
    while t >0:
        maxh = lst.index(max(lst))
        less = lst.index(min(lst))
        lst[maxh] -= 1
        lst[less] += 1
        t -= 1
        
    value =  max(lst)-min(lst)
    print("#{} {}".format(i, value))

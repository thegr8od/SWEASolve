#1244 최대상금
t = int(input())

for tc in range(1,t+1):
    data, n = input().split()
    n = int(n)
    lst = []
    for i in data:
        lst.append(i)
    v = []
    l = len(data)
    ans = 0
    def dfs(x):
        global ans
        if x == n:
            ans = max(ans,int("".join(map(str,lst))))
            return
        for i in range(l-1):
            for j in range(i+1, l):
                lst[i], lst[j] = lst[j], lst[i]
                chk = int("".join(map(str, lst)))
                if (x,chk) not in v:
                    dfs(x+1)
                    v.append((x,chk))
                lst[j], lst[i] = lst[i], lst[j]
    
    dfs(0)
    print("#{} {}".format(tc,ans))
                      
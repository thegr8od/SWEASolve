t = int(input())

for tc in range(1,t+1):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    
    ans = 0
    def dfs(x,score):
        global ans
        if score == k:
            ans += 1
            return
        if x == n:
            return
        if score > k:
            return

        dfs(x+1, score+data[x])
        dfs(x+1, score)
        
    dfs(0,0)
    print("#{} {}".format(tc, ans))
    
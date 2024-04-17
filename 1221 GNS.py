t = int(input())

num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1,t+1):
    t,c = input().split()
    data = list(input().split())
    ans = []
    for i in range(int(c)):
        ans.append(num.index(data[i]))
    
    ans.sort()
    
    for j in range(int(c)):
        ans[j] = num[ans[j]]
        
    print("{}".format(t))
    print(*ans)
        
        
    
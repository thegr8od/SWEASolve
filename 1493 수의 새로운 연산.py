t= int(input())
for tc in range(1,t+1):
    p, q = map(int, input().split())
    p_a = 0
    q_a = 0
    for i in range(200):
        if p > 0:
            p = p-i
            p_a = i
        if q > 0:
            q = q-i
            q_a = i
    
    p_x = p_a + p
    p_y = abs(p)+1
    q_x = q_a + q
    q_y = abs(q)+1
    
    ans_x = p_x + q_x
    ans_y = p_y + q_y
    ans = 0
    
    for i in range(ans_x + ans_y -1):
        ans += i
    ans += ans_x
    
    print("#{} {}".format(tc, ans))
        
    
    
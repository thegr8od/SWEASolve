t = int(input())

for tc in range(1,t+1):
    d,l,n = map(int, input().split())
    total_d = d
    for i in range(1,n):
        now_damage = d * (1+i * (l/100))
        total_d += now_damage
        
    print("#{} {}".format(tc,int(total_d)))
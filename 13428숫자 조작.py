t = int(input())

for tc in range(1,t+1):
    n = list(input())
    l = len(n)
    gi = 10 ** (l-1)
    minv = int("".join(map(str,n)))
    maxv = int("".join(map(str,n)))
    for i in range(l-1):
        for j in range(i,l):
            n[i], n[j] = n[j], n[i]
            if int("".join(map(str,n))) >= gi:
                minv = min(minv, int("".join(map(str,n))))
                maxv = max(maxv, int("".join(map(str,n))))
            n[j], n[i] = n[i], n[j]    
    print("#{} {} {}".format(tc,minv, maxv))
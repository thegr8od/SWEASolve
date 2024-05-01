for _ in range(10) :
    T = int(input())
    N, M = map(int, input().split())

    def power(a, n):
        if n == 1:
            return a
        
        return power(a, n-1) * a
    
    print("#{} {}".format(T, power(N, M)))
    
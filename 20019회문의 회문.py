def palindrome(s):
    if s == s[::-1]:
        return 1
    else:
        return 0
    
t = int(input())
for tc in range(1, t+1):
    st = input()
    is_pal = 0
    
    if palindrome(st):
        if palindrome(st[0:(len(st)-1)//2]):
            if palindrome(st[(len(st)+1//2):]):
                is_pal = 1
    
    if is_pal == 1:
        print("#{} YES".format(tc))
    else:
        print("#{} NO".format(tc))
                    
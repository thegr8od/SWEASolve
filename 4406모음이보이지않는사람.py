t = int(input())

for i in range(t):
    word = list(input())
    print(word)
    ans = []
    for j in word:
        if j !='a' and j != 'e' and j != 'i' and j != 'o' and j != 'u':
            ans.append(j)
    
    ans1 = "".join(ans)
    print("#{} {}".format(i+1, ans1))
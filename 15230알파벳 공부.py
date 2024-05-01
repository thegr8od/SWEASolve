t = int(input())
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 
 
 
 
for tc in range(1,t+1):
    cnt = 0
    data = list(input())
    if data[0] == 'a':
        for i in range(len(data)):
            if data[i] == alphabet[cnt]:
                cnt+=1
            else:
                break   
        print("#{} {}".format(tc, cnt))     
    else:
        print("#{} {}".format(tc, 0))
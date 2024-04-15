t = int(input())

for tc in range(1,t+1):
    text = list(input())
    new_text = text[::-1]
    for i in range(len(new_text)):
        if new_text[i] == 'b':
            new_text[i]  = 'd'
        elif new_text[i]  == 'p':
            new_text[i]  = 'q'
        elif new_text[i]  == 'd':
            new_text[i]  = 'b'
        elif new_text[i]  == 'q':
            new_text[i]  = 'p'
    print("#{} ".format(tc),end='')
    print(*new_text,sep='')
    
t = int(input())

for tc in range(1,t+1):
    s_answer = 13
    d_answer = 13
    h_answer = 13
    c_answer = 13
    card_set = set()
    
    data = list(input())
    for i in range(len(data)):
        if data[i] == 'S':
            s_answer -= 1
            card_set.add(data[i]+data[i+1]+data[i+2])
        elif data[i] == 'D':
            d_answer -= 1
            card_set.add(data[i]+data[i+1]+data[i+2])
        elif data[i] == 'H':
            h_answer -= 1
            card_set.add(data[i]+data[i+1]+data[i+2])
        elif data[i] == 'C':
            c_answer -= 1
            card_set.add(data[i]+data[i+1]+data[i+2])
    if len(card_set) == (len(data) // 3):
        print("#{} {} {} {} {}".format(tc,s_answer,d_answer,h_answer,c_answer))
    else:
        print("#{} ERROR".format(tc))
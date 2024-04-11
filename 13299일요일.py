t = int(input())

for tc in range(1, t+1):
    s = input()
    num = 0
    if s == "SUN":
        num = 7
    elif s == "MON":
        num = 6
    elif s == "TUE":
        num = 5
    elif s == "WED":
        num = 4
    elif s == "THU":
        num = 3
    elif s == "FRI":
        num = 2
    elif s == "SAT":
        num = 1
    print("#{} {}".format(tc, num))
        
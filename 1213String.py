for tc in range(1,11):
    n = int(input())
    string = input()
    sentence = input()

    count = sentence.count(string)
    print("#{} {}".format(n, count))
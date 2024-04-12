t = int(input())

for tc in range(1,t+1):
    text = list(input())
    
    first_line = '..#.'
    second_line = '.#.#'
    fourth_line = '.#.#'
    fifth_line = '..#.'
    middle_line = ''
    
    for i in range(len(text)):
        middle_line += '#.' + text[i] + '.'
        
    print(first_line * len(text) + '.')
    print(second_line * len(text) + '.')
    print(middle_line + '#')
    print(fourth_line * len(text) + '.')
    print(fifth_line * len(text) + '.')
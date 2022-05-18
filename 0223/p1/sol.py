import sys
sys.stdin = open('input.txt')


# tc 입력
for tc in range(int(input())):
    char = input()
    stack = []
    change_char = ''
    pop_stack = ''
    for i in char:
        if i == '+' or i == '-' or i == '*' or i == '/':
            stack.append(i)
        else:
            change_char += i
    for j in stack:
        pop_stack = j + pop_stack
    change_char += pop_stack
    print(change_char)


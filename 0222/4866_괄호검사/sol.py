import sys
sys.stdin = open('input.txt')

def str_len(x):
    cnt = 0
    for i in x:
        cnt += 1
    return cnt

def push(x, N):
    global top
    top += 1
    if top == N:
        print('overflow')
    else:
        stack[top] = x

def pop():
    global top
    top -= 1
    return stack[top+1]

# tc 입력
for tc in range(int(input())):
    char = input()
    N = str_len(char)
    stack = [0] * (N)
    top = -1
    result = 0
    for i in char:
        if i == '(' or i == '{':
            push(i, N)
        elif top > -1:
            if i == ')' and stack[top] == '(':
                pop()
            elif i == ')' and stack[top] != '(':
                result = 2
                break
            if i == '}' and stack[top] == '{':
                pop()
            elif i == '}' and stack[top] != '{':
                result = 2
                break
        elif top == -1:
            if i == ')' or i == '}':
                result = 2
                break
    if top == -1 and result == 0:
        result = 1
    elif top != -1 or result == 2:
        result = 0
    print(f'#{tc+1} {result}')

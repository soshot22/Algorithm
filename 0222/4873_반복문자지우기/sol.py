import sys
sys.stdin = open('input.txt')
# 문자열 길이 함수
def str_len(char):
    cnt = 0
    for i in char:
        cnt += 1
    return cnt
# push
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
    stack = [0] * N
    top = -1
    for i in char:
        if i != stack[top]:
            push(i, N)
        elif top >= 0 and i == stack[top]:
            pop()
    print(f'#{tc+1} {top+1}')

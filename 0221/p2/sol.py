import sys
sys.stdin = open('input.txt')
def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top + 1]

for tc in range(int(input())):
    arr = [i for i in input()]
    top = -1
    stack = [0] * len(arr)
    for i in arr:
        if i == '(':
            push(i, len(arr))
        elif i == ')' and stack[top] == '(':
            pop()
        elif i == ')' and stack[top] != '(':
            break

    if stack[top] == 0:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc + 1} -1')

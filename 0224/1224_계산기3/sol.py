import sys
sys.stdin = open('input.txt')

# 후기표기법으로 변환할 함수
def after(x):
    # 시작점이자 비교점으로 활용
    stack = [0]
    # 변환시킨 내용을 담을 함수
    result = []
    for i in x:
        # + 우선순위가 제일 아래
        if i == '+':
            # +, * 들을 모두 pop
            while stack[-1] == '*' or stack[-1] == '+':
                result.append(stack.pop())
            # 스택에 저장
            stack.append(i)
            # * 우선순위가 제일 위이니 바로 push
        elif i == '*':
            stack.append(i)
            # ( 는 추가
        elif i == '(':
            stack.append(i)
            # ( 이전까지 pop하고 (도 pop
        elif i == ')':
            while stack[-1] == '*' or stack[-1] == '+':
                result.append(stack.pop())
            stack.pop()
            # 그외 피 연산자는 모두 반환할 값에 추가
        else:
            result.append(i)
    # 시작에 나둔 0을 제외해야 하므로 len(stack) -1
    for i in range(len(stack)-1):
        result.append(stack.pop())
    # 후기표기법으로 변환한 값 반환
    return result

# 후기표기 계산식 계산
def cal(x):
    stack = []
    for i in x:
        # * 와 + 는 좌우 교환이 가능하므로 바로 계산
        if i == '*':
            j = stack.pop() * stack.pop()
            stack.append(j)
        elif i == '+':
            k = stack.pop() + stack.pop()
            stack.append(k)
        # 피연산자는 문자형식이었으니 정수형으로 변환후 추가
        else:
            stack.append(int(i))
    # 최종 계산된 값 반환
    return stack[0]

for tc in range(10):
    N = int(input())
    char = input()
    print(f'#{tc+1} {cal(after(char))}')
import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    stack = []
    # 계산식 리스트로 변환해서 받기
    case = list(input().split())
    # 에러 확인에 사용할 리스트
    error_list = ['+', '-', '*', '/']
    # 입력받은 계산식을 순회
    for i in case:
        # 사용할 피연산자가 2개가 안되는 경우
        if len(stack) < 2 and i in error_list:
            result = 'error'
            break
        # 각 사칙연산에 따라 스택 제일 마지막과 그 앞 수 계산
        elif i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        # -와 / 는 순서가 필요하므로 고려해서 계산
        elif i == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        # 나누어 떨어진다고 했으므로 정수형 유지를 위해 //
        elif i == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b // a)
        # 마지막 .에 도달했을 때 스택에 1개 초과면 error 표시
        elif i == '.':
            if len(stack) > 1:
                result = 'error'
            else:
                result = int(stack.pop())
        # 피연산자는 스택에 push
        else:
            stack.append(int(i))
    print(f'#{tc+1} {result}')
import sys
sys.stdin = open('input.txt')
# 해당 수에 *2를 하여 1을 넘긴 부분은 -1(이진수 1)
# 1을 못 넘긴 경우(이진수 0)
for tc in range(1, int(input()) + 1):
    N = float(input())
    result = ''
    while N != 0:  # N이 0이 아닌 경우
        N *= 2  # N에 2를 곱해줌
        if N >= 1:  # 1를 초과하는 경우
            result += '1'
            N -= 1
        else:  # 곱을 해도 1보다 작은 경우
            result += '0'
    print(f'{tc}', end=' ')
    if len(result) >= 13:  # 13자리 넘어 갔는 지 확인
        print('overflow')
    else:
        print(result)
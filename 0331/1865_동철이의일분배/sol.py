import sys
sys.stdin = open('input.txt')

# 인자(일의 위치, 현재까지 확률)
def work(n, p):
    global result
    # 0<x<= 1 이면 a*x <= a 확률은 1이하이므로 곱해도 더 높아질 수 없음
    if p <= result:
        return
    # 모든 업무가 할당된 경우
    if n == N:
        # 기존 확률 보다 더 높을 경우
        if p > result:
            result = p
        return
    # 모든 작업자 순회
    for i in range(N):
        # 해당 작업자에게 할당이 없는 경우
        if visited[i] == 0:
            # 할당
            visited[i] = 1
            # 다음 제품의 할당자 선택으로 이동
            work(n+1, p * arr[n][i])
            # 할당 없애기
            visited[i] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    # 람다를 활용해서 백분위로 인자 입력
    arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 0
    work(0, 1)
    result *= 100
    print(f'#{tc} ', end='')
    print('%.6f' % result)
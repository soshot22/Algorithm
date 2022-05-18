import sys
sys.stdin = open('input.txt')

# 함수 인자(현재 선택할 상품 번호, 현재까지 비용)
def product(n, ssum):
    global result
    # 가지치기 이미 기존 최솟값 초과시 종료
    if ssum >= result:
        return
    # 모든 제품에 대한 나라 선택 완료
    if n == N:
        # 최솟값보다 작으면 교체
        if ssum < result:
            result = ssum
    # N가지 국가 모두 순회
    for i in range(N):
        # 아직 국가를 선택한 적 없으면
        if visited[i] == 0:
            # 선택 표시 후 다시 함수에 입력
            visited[i] = 1
            product(n+1, ssum + arr[n][i])
            # 같은 제품 단계에서 다른 국가 선택을 위해 선택표시 제거
            visited[i] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())                    # 공장 수 및 제품 수
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 99 * N + 1
    product(0, 0)
    print(f'#{tc} {result}')
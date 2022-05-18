import sys
sys.stdin = open('input.txt')

# 최소값을 확인할 함수(현재위치, 방문 횟수, 배터리 사용량)
def f(n, k, ssum):
    # 1을 제외하고 나머지 N-1 모두 방문 시
    if k == N-1:
        # 다시 사무실로 돌아오는 사용량 더 해줌
        ssum += arr[n][0]
        # 배터리 사용량이 이전 최솟값보다 적다면 교체
        global result
        if result > ssum:
            result = ssum
    # N-1가지 경우의 수 확인(사무실 제외)
    for i in range(1, N):
        # 아직 방문하지 않았다면
        if visited[i] == 0:
            # 방문 표시
            visited[i] = 1
            # i를 출발값으로 변경
            f(i, k+1, ssum + arr[n][i])
            # 방문 표시 초기화
            visited[i] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 방문 표시 리스트
    visited = [0] * N
    # 100 이하의 자연수 이므로
    result = 100 * N + 1
    # 함수 적용
    f(0,0,0)
    print(f'#{tc} {result}')
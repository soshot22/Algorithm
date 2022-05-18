import sys
sys.stdin = open('input.txt')

# 방향 변수(우,하)
di = [[0, 1], [1, 0]]

# 각 위치에서 시작하는 값들을 찾을 함수(행, 열, 합계)
def f(i, j, ssum):
    global result
    # 가지치기, 이미 최소값 희망 x면 종료
    if ssum >= result:
        return
    # 종료조건 제일 우측 아래 도달
    if i == N-1 and j == N-1:
        # 최솟값보다 작다면
        if ssum < result:
            result = ssum
    else:
        # 2가지 방향으로 이동
        for k in range(2):
            ni, nj = i + di[k][0], j + di[k][1]
            # 우하로만 이동하니 0보다는 무조건 큼, 이전으로 돌아 갈수 없음
            if ni <= N-1 and nj <= N-1:
                # 새롭게 재귀로 돌아감
                f(ni, nj, ssum + arr[ni][nj])

for tc in range(1, int(input()) + 1):
    # NxN 행렬의 N 입력
    N = int(input())
    # NxN 행렬의 각 인지 입력
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 임의의 최대값
    result = 10 * N * N + 1
    # 제일 좌측 위에서 시작하며 arr[0][0] 값이 합의 기본값
    f(0, 0, arr[0][0])
    print(f'#{tc} {result}')
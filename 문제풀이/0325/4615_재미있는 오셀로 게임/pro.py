import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    # 좌표가 1부터 시작하므로
    arr = [[0] * (N+1) for _ in range(N+1)]
    # 기본 돌 배치 백흑 순
    arr[N//2][N//2] = arr[N//2 + 1][N//2 + 1] = 2
    arr[N//2+1][N//2] = arr[N//2][N//2 + 1] = 1
    # M번 돌 놓기
    for _ in range(M):
        # 입력받은 돌을 넣기
        sj, si, d = map(int, input().split())
        arr[si][sj] = d
        # 8방향 상좌 상 상우 하좌 하 하우 좌 우 순
        for di, dj in ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)):
            s = []
            # 방향에 맞게 순회할 함수
            for k in range(1, N):
                # 해당 방향에 맞게 새로 설정한 좌표
                ni, nj = si + di*k, sj + dj*k
                # 좌표가 행렬 범위 안인 경우
                if 1 <= ni <= N and 1 <= nj <= N:
                    # 빈 공간이면 멈춤
                    if arr[ni][nj] == 0:
                        break
                    # 색 바꿔줌
                    elif arr[ni][nj] == d:
                        for ci, cj in s:
                            arr[ci][cj] = d
                        break
                    # 다른 색이면 바꿀 리스트에 추가
                    else:
                        s.append((ni, nj))
                else:
                    break
    # 각 돌의 수
    bcnt = wcnt = 0
    # 각 좌표를 순회
    for lst in arr:
        # 각 수에 맞는
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{tc} {bcnt} {wcnt}')
import sys
sys.stdin = open('input.txt')

# 방향 상하좌우
di = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 행좌표, 열좌표, 현재 최대수직이동거리
def F(x, y, m):
    global result
    if m >= result:
        return
    # 목표지점을 도착한 경우
    if arr[x][y] == 3:
        # 현재 최소횟수랑 비교해서 더 작은 경우 교체
        if m < result:
            result = m
        return
    
    for i in range(4):
        # 방향이 상 or 하인 경우
        if i <= 1:
            # 모든 영역 확인
            for j in range(1, N):
                ni, nj = x + di[i][0]*j, y + di[i][1]*j
                # 최대이동값 이상시 무의미
                if j >= result:
                    visited[x][y] = 1
                    break
                # 범위 밖인 경우 중지
                if ni > N-1 or ni < 0 or nj > M-1 or nj < 0:
                    break
                # 방문 시 종료(이전보다 더 아래로 가는 것은 의미x)
                if visited[ni][nj] == 1:
                    break
                #  미방문시이고 이동 가능한 경우
                if arr[ni][nj] != 0:
                    # 방문 표시
                    visited[ni][nj] = 1
                    # 최대 수직이동 횟수 변경
                    if j > m:
                        F(ni, nj, j)
                    # 최대 이동 횟수 유지
                    else:
                        F(ni, nj, m)
                    # 방문표시 지우기
                    visited[ni][nj] = 0
                    # 더 위는 확인x
                    break
        # 좌우 확인
        else:
            ni, nj = x + di[i][0], y + di[i][1]
            if 0 <= ni <= N-1 and 0 <= nj <= M - 1 and visited[ni][nj] == 0 and arr[ni][nj] != 0:
                # 방문 표시
                visited[ni][nj] = 1
                F(ni, nj, m)
                visited[ni][nj] = 0



for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    # 시작점 방문표시
    visited[N-1][0] = 1
    # 최솟값 설정
    G =[]
    result = 0
    for i in range(N-1):
        for j in range(M):
            if arr[i][j] == 3:
                G += [i, j]
                break
        if G:
            break
    cnt = 1
    max_height = 0
    result = N-1 - G[0]
    for i in range(G[0], N):
        if arr[i][G[1]] == 0:
            cnt += 1
        else:
            if cnt > max_height:
                max_height = cnt
            cnt = 1
    if max_height < result:
        result = max_height
    F(N-1, 0, 0)
    print(f'#{tc} {result}')
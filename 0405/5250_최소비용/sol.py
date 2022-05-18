import sys
sys.stdin = open('input.txt')

def f():
    # 큐 생성 및 시작지점 추가
    queue = []
    queue.append([0, 0])
    # N은 최대 100 H는 최대 1000
    visited = [[500*N +200] * N for _ in range(N)]
    visited[0][0] = 0
    while queue:
        i, j = queue.pop(0)
        # 상하좌우
        for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            ni, nj = i + di, j + dj
            # 상하좌우가 만약 범위 내라면
            if 0 <= ni <= N-1 and 0 <= nj <= N-1:
                # 현재 위치 + 1 + 현재위치와 새방문 위치 높이 차(0 or 양수)
                new = visited[i][j] + 1 + max(arr[ni][nj] - arr[i][j], 0)
                # 해당경로로 방문 시 더 최소값이면 교체 밑 경로로 넣기
                if visited[ni][nj] > new:
                    visited[ni][nj] = new
                    queue.append([ni, nj])
    return visited[N-1][N-1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = f()
    print(f'#{tc} {result}')
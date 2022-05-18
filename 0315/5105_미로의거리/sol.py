import sys
sys.stdin = open('input.txt')

# bfs 함수(시작 행, 시작 열)
def bfs(i, j):
    # 방문을 표시할 NxN 행렬
    visited = [[0] * N for _ in range(N)]
    # queue 생성
    queue = []
    # queue에 시작점 추가
    queue.append([i, j])
    # 시작점 방문 표시
    visited[i][j] = 1
    # 큐에 남은 것이 있는 한 반복
    while queue:
        # 큐에서 뽑아서 행,렬
        i, j = queue.pop(0)
        # 4방향 확인 반복
        for di, dj in [[0, 1], [1,0], [0,-1],[-1,0]]:
            ni, nj = i +di, j +dj
            # ni, nj의 범위, 미로가 통로(1이 아님), 방문x
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                # 새로운 지점 큐에 추가
                queue.append([ni, nj])
                # 만약 도착지점이라면 출발점을 제외한 값 반환
                if maze[ni][nj] == 3:
                    return visited[i][j] - 1
                # 방문 표시(기존 지점 +1)
                visited[ni][nj] = visited[i][j] + 1
    # 도착지점을 찾지 못했다면
    return 0

for tc in range(int(input())):
    # 미로의 크기 입력
    N = int(input())
    # 미로 입력
    maze = [list(map(int, input())) for _ in range(N)]
    # 시작 지점 찾기
    start_i = 0
    start_j = 0
    for_break = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_i = i
                start_j = j
                for_break = 1
                break
        if for_break:
            break
    # bfs함수에 시작지점을 인자로 값 구하기
    result = bfs(start_i, start_j)
    print(f'#{tc+1} {result}')
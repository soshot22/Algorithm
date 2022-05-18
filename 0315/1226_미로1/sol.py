import sys
sys.stdin = open('input.txt')

def bfs(i, j):
    # 방문 표시할 16x16 행렬 생성
    visited = [[0] * 16 for _ in range(16)]
    # 큐 생성
    queue = []
    # 큐에 시작지점 추가
    queue.append([i, j])
    # 방문 표시
    visited[i][j] = 1
    # 큐에 인자가 있는 동안 반복
    while queue:
        # 시작 지점은 큐의 첫인자
        i, j = queue.pop(0)
        # 우 하 좌 상 방향
        for di, dj in [[0, 1], [1,0], [0,-1],[-1,0]]:
            ni, nj = i + di, j + dj
            # 각 값이 미로 범위 내이고 길이 있으며 방문하지 않은 경우
            if 0 <= ni < 16 and 0 <= nj < 16 and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                # 도착지점에 도착한 경우 1 반환
                if maze[ni][nj] == 3:
                    return 1
                # 도착 지점이 아닌 경우 큐에 좌표 추가 및 방문 표시
                queue.append([ni, nj])
                visited[ni][nj] = 1
    return 0

for _ in range(10):
    # tc, 및 반복입력
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    # 반복문 종료를 위한 변수
    end = 0
    for i in range(16):
        for j in range(16):
            # 출발점을 찾으면 변수로 저장
            if maze[i][j] == 2:
                start_i = i
                start_j = j
                end += 1
                break
        if end:
            break
    # 출력에 맞춰 함수 입력
    print(f'#{tc} {bfs(start_i, start_j)}')
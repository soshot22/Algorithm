import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    bp = 0
    result = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_i, start_j = i, j
            elif arr[i][j] == 3:
                end_i, end_j = i, j
    queue = []
    queue.append([start_i, start_j])
    visited[start_i][start_j] = 1
    end = 0
    while queue:
        if end == 1:
            break
        i, j = queue.pop(0)
        for k in range(4):
            ni, nj = i + dir[k][0], j + dir[k][1]
            if 0 <= ni <= N - 1 and 0 <= nj <= N - 1 and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = visited[i][j] + 1
                if arr[ni][nj] == 3:
                    end = 1
                    break
    result = visited[end_i][end_j] - 2
    if result < 0:
        result = 0
    print(f'#{tc} {result}')

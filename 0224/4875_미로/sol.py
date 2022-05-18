import sys
sys.stdin = open('input.txt')

def f(arr, x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    stack_x = []
    stack_y = []
    while x != -1 and y != -1:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                if arr[nx][ny] == '0' and visited[nx][ny] == 0:
                    stack_x.append(x)
                    stack_y.append(y)
                    visited[nx][ny] = 1
                    x = nx
                    y = ny
                    break
                elif arr[nx][ny] == '3':
                    return 1
        else:
            if stack_x:
                x = stack_x.pop()
                y = stack_y.pop()
            else:
                x = -1
    return 0

for tc in range(int(input())):
    N = int(input())
    miro = [[i for i in input()] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if miro[i][j] == '2':
                start_x = i
                start_y = j
    result = f(miro, start_x, start_y)
    print(f'#{tc + 1} {result}')
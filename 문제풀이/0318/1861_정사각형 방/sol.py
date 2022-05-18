import sys
sys.stdin = open('input.txt')

def bfs(x, y):
    global visited
    s_i = x
    s_j = y
    visited[s_i][s_j] = 1
    cnt = 0
    while s_i > -1:
        for i in range(4):
            ni = s_i + di[i]
            nj = s_j + dj[i]
            if 0 <= ni <= N-1 and 0 <= nj <= N-1:
                if arr[s_i][s_j] + 1 == arr[ni][nj]:
                    visited[ni][nj] = visited[s_i][s_j] + 1
                    s_i = ni
                    s_j = nj
                    if visited[ni][nj] > cnt:
                        cnt = visited[ni][nj]
                    break
        else:
            return cnt

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [[0] *N for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    for i in range(N):
        a = list(map(int, input().split()))
        for j in range(N):
            arr[i][j] = a[j]
    max_cnt = 0
    visited = [[0] * N for _ in range(N)]
    room_num = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                b = bfs(i, j)
                if b > max_cnt:
                    max_cnt = b
                    room_num = arr[i][j]
                elif b == max_cnt:
                    if arr[i][j] < room_num:
                        room_num = arr[i][j]

    print(f'#{tc} {room_num} {max_cnt}')

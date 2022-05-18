import sys
sys.stdin = open('input.txt')

def bfs(x, y):
    global L
    s_i = x
    s_j = y
    visitied[s_i][s_j] = 1
    queue = []
    queue.append([s_i, s_j])
    cnt = 0
    L -= 1
    now = 1
    while L:
        s_i, s_j = queue.pop(0)
        level = visitied[s_i][s_j]
        if level > now:
            L -= 1
            now = level
            if L == 0:
                break
        # 1은 4방향(range4)
        if arr[s_i][s_j] == 1:
            for i in range(4):
                ni = s_i + di[i]
                nj = s_j + dj[i]
                if 0<= ni <= N-1 and 0<= nj <= M-1 and arr[ni][nj] != 0 and visitied[ni][nj] == 0:
                    if arr[ni][nj] in pipe[i]:
                        visitied[ni][nj] = visitied[s_i][s_j] + 1
                        queue.append([ni, nj])
        # 2는 상하(range2)
        elif arr[s_i][s_j] == 2:
            for i in range(2):
                ni = s_i + di[i]
                nj = s_j + dj[i]
                if 0 <= ni <= N - 1 and 0 <= nj <= M - 1 and arr[ni][nj] != 0 and visitied[ni][nj] == 0:
                    if arr[ni][nj] in pipe[i]:
                        visitied[ni][nj] = visitied[s_i][s_j] + 1
                        queue.append([ni, nj])
        # 3은 좌우(range(2,4))
        elif arr[s_i][s_j] == 3:
            for i in range(2, 4):
                ni = s_i + di[i]
                nj = s_j + dj[i]
                if 0 <= ni <= N - 1 and 0 <= nj <= M - 1 and arr[ni][nj] != 0 and visitied[ni][nj] == 0:
                    if arr[ni][nj] in pipe[i]:
                        visitied[ni][nj] = visitied[s_i][s_j] + 1
                        queue.append([ni, nj])
        # 4는 상우(range(0,4,3)
        elif arr[s_i][s_j] == 4:
            for i in range(0, 4, 3):
                ni = s_i + di[i]
                nj = s_j + dj[i]
                if 0 <= ni <= N - 1 and 0 <= nj <= M - 1 and arr[ni][nj] != 0 and visitied[ni][nj] == 0:
                    if arr[ni][nj] in pipe[i]:
                        visitied[ni][nj] = visitied[s_i][s_j] + 1
                        queue.append([ni, nj])
        # 5 하우(range(1,4,2))
        elif arr[s_i][s_j] == 5:
            for i in range(1, 4, 2):
                ni = s_i + di[i]
                nj = s_j + dj[i]
                if 0 <= ni <= N - 1 and 0 <= nj <= M - 1 and arr[ni][nj] != 0 and visitied[ni][nj] == 0:
                    if arr[ni][nj] in pipe[i]:
                        visitied[ni][nj] = visitied[s_i][s_j] + 1
                        queue.append([ni, nj])
        #  6 하좌(range(1,3)
        elif arr[s_i][s_j] == 6:
            for i in range(1, 3):
                ni = s_i + di[i]
                nj = s_j + dj[i]
                if 0 <= ni <= N - 1 and 0 <= nj <= M - 1 and arr[ni][nj] != 0 and visitied[ni][nj] == 0:
                    if arr[ni][nj] in pipe[i]:
                        visitied[ni][nj] = visitied[s_i][s_j] + 1
                        queue.append([ni, nj])
        # 7 상좌(range(0,4,2))
        elif arr[s_i][s_j] == 7:
            for i in range(0, 4, 2):
                ni = s_i + di[i]
                nj = s_j + dj[i]
                if 0 <= ni <= N - 1 and 0 <= nj <= M - 1 and arr[ni][nj] != 0 and visitied[ni][nj] == 0:
                    if arr[ni][nj] in pipe[i]:
                        visitied[ni][nj] = visitied[s_i][s_j] + 1
                        queue.append([ni, nj])
        if queue:
            continue
        else:
            break
    for k in range(N):
        for l in range(M):
            if visitied[k][l] > 0:
                cnt += 1
    return cnt

for tc in range(1, int(input())+1):
    # 지하도 세로 N, 가로 M / 맨홀 세로 R, 가로 C / 시간 L
    N, M, R, C, L = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for i in range(N):
        ls = list(map(int, input().split()))
        for j in range(M):
            arr[i][j] = ls[j]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    pipe = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]
    start_i = R
    start_j = C
    visitied = [[0] * M for _ in range(N)]
    print(f'#{tc} {bfs(start_i, start_j)}')
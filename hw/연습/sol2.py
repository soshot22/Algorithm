import sys
sys.stdin = open('input.txt')
# 6방향
di_1 = [[-1, 0],[1,0],[-1,1],[0,1],[-1,-1],[0,-1]]
di_2 = [[-1, 0],[1,0],[0,1],[1,1],[0,-1],[1,-1]]

def F(i, j, n, plus):
    if n == 0:
        global result
        if plus**2 > result:
            result = plus**2
        return
    if j % 2:
        for k in range(6):
            ni, nj = i + di_2[k][0], j + di_2[k][1]
            if 0 <= ni <= H-1 and 0 <= nj <= W-1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                F(ni, nj, n-1, plus + arr[ni][nj])
                F(i, j, n - 1, plus + arr[ni][nj])
                visited[ni][nj] = 0
    else:
        for k in range(6):
            ni, nj = i + di_1[k][0], j + di_1[k][1]
            if 0 <= ni <= H-1 and 0 <= nj <= W-1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                F(ni, nj, n-1, plus + arr[ni][nj])
                F(i, j, n-1, plus + arr[ni][nj])
                visited[ni][nj] = 0



for tc in range(1, int(input())+1):
    # 가로W 세로 H
    W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    result = 0
    for i in range(H):
        for j in range(W):
            visited = [[0]*W for _ in range(H)]
            visited[i][j] = 1
            F(i, j, 3, arr[i][j])
    print(f'#{tc} {result}')

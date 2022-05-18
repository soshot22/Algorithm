import sys
sys.stdin = open('input.txt')
''' 가능한 모든 경우 > 정답
대각선은 행 + 열의 값이 N으로 고정됨 및 같은 수
[0,3] [1,2], [2,1], [3,0] / [0,0],[1,1]
'''
# 자신보다 위의 행 위치에 n이 있는 지 확인(위, 좌상, 우상)
def check(si, sj):
    # 위쪽방향
    for i in range(si-1, -1, -1):
        if visited[i][sj] == 1:
            return 0
    # 좌측 대각선 위
    i, j = si-1, sj-1
    while i >= 0 and j >= 0:
        if visited[i][j] == 1:
            return 0
        i, j = i-1, j-1
    # 우측 대각선 위
    i, j = si - 1, sj + 1
    while i >= 0 and j < N:
        if visited[i][j] == 1:
            return 0
        i, j = i - 1, j + 1
    return 1

def DFS(n):
    global result
    if n == N:
        result += 1
        return
    for j in range(N):
        if check(n, j):
            visited[n][j] = 1
            DFS(n+1)
            visited[n][j] = 0

def DFS_1(n):
    global result
    if n == N:
        result += 1
        return
    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == 0:
            v1[j] = v2[n+j] = v3[n-j] = 1
            DFS_1(n+1)
            v1[j] = v2[n+j] = v3[n-j] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    result = 0
    visited = [[0]*N for _ in range(N)]
    #DFS(0)
    print(f'#{tc} {result}')

    # 다른 방식
    v1, v2, v3 = [0] * 30, [0]* 30, [0] * 30
    DFS_1(0)
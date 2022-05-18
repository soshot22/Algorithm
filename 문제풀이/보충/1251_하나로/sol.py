import sys
sys.stdin = open('input.txt')

def BFS(k, n):
    if n == N:
        for i in range(1, N):
            (x_ls[i] - x_ls[visited[i]])**2 + (y_ls[i] - y_ls[visited[i]])**2

    for i in range(k+1, N):
        if visited[i] == 0:
            visited[i] = k
            BFS(i, n+1)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    x_ls = [0] + list(map(int, input().split()))
    y_ls = [0] + list(map(int, input().split()))
    E = float(input())
    visited = [0] *(N + 1)

    result = 0
    print(f'#{tc} {result}')
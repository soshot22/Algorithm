import sys
sys.stdin = open('input.txt')

def bfs(arr, s):
    visited = [0] * (N+1)
    queue = []
    queue.append(s)
    visited[s] = 1
    print(f'-{s}', end = '')
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = 1
            print(f'-{t}', end='')
        for i in range(N+1):
            if arr[t][i] == 1 and visited[i] == 0:
                queue.append(i)
    return





N, E = map(int, input().split())
line_arr = list(map(int, input().split()))
arr = [[0] * (N+1) for _ in range(N+1)]
for i in range(E):
    arr[line_arr[i*2]][line_arr[i*2 + 1]] = 1
    arr[line_arr[i * 2 + 1]][line_arr[i * 2]] = 1
bfs(arr, 1)


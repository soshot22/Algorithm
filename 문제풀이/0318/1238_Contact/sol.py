import sys
sys.stdin = open('input.txt')

def bfs(arr, s):
    queue = []
    visited = [0] * (N+1)
    queue.append(s)
    visited[s] = 1
    while queue:
        s = queue.pop(0)
        for i in range(1, N+1):
            if link_map[s][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[s] + 1
        else:
            if queue:
                pass
            else:
                result = 0
                for i in range(1, N+1):
                    if visited[i] >= visited[result]:
                        result = i
                return result

for tc in range(1, 11):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))
    link_map = [[0] * (N+1) for _ in range(N+1)]
    for i in range(len(arr)//2):
        link_map[arr[i*2]][arr[i*2 + 1]] = 1
    bfs(link_map, start)
    print(f'#{tc} {bfs(link_map, start)}')
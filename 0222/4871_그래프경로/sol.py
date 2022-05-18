import sys
sys.stdin = open('input.txt')
def f(arr, start, end):
    stack = []
    visited = [0] * (V+1)
    while start:
        for d in range(1, V+1):
            if arr[start][d] == 1 and visited[d] == 0:
                stack.append(start)
                visited[d] = 1
                start = d
                break
        else:
            if stack:
                start = stack.pop()
            else:
                break
    if visited[end] == 1:
        return 1
    else:
        return 0

for tc in range(int(input())):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        x, y = map(int, input().split())
        arr[x][y] = 1
    S, G = map(int, input().split())
    print(f'#{tc+1} {f(arr, S, G)}')

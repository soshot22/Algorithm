import sys
sys.stdin = open('input.txt')

N, E = map(int, input().split())
arr = [list([0]*(N+1)) for _ in range(N+1)]
line_ls = list(map(int, input().split()))
for i in range(E):
    arr[line_ls[i*2]][line_ls[i*2 + 1]] = 1
    arr[line_ls[i*2 + 1]][line_ls[i*2]] = 1
visited = [0] * (N+1)
start = 1
stack = []
print(start, end = ' ')
visited[start] = 1
while start:
    for y in range(N+1):
        if arr[start][y] == 1 and visited[y] == 0:
            visited[y] = 1
            stack.append(start)
            start = y
            print(y, end = ' ')
            break
    else:
        if stack:
            start = stack.pop()
        else:
            start = 0



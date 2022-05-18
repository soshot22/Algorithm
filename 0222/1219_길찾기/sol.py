import sys
sys.stdin = open('input.txt')

def f(arr):
    start = 0
    end = 99
    stack = []
    visited = [0] * 100
    while start > -1:
        for i in range(2):
            if arr[i][start] != 0 and visited[arr[i][start]] == 0:
                visited[arr[i][start]] = 1
                stack.append(start)
                start = arr[i][start]
                break
        else:
            if stack:
                start = stack.pop()
            else:
                start = -1
    if visited[end] == 1:
        return 1
    else:
        return 0

for _ in range(10):
    TC, N = map(int, input().split())
    line_arr = list(map(int, input().split()))
    arr = [list([0]*100) for l in range(2)]
    for i in range(N):
        if arr[0][line_arr[2*i]] == 0:
            arr[0][line_arr[2*i]] = line_arr[2*i + 1]
        else:
            arr[1][line_arr[2*i]] = line_arr[2*i + 1]
    print(f'#{TC} {f(arr)}')






# print(f'#{TC} {f(arr, S, G)}')
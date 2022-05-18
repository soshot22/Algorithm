import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for x in range(N):
        cnt = 0
        for y in range(N):
            if arr[x][y] == 1:
                cnt += 1
            elif arr[x][y] == 0 and cnt != K:
                cnt = 0
            elif arr[x][y] == 0 and cnt == K:
                result += 1
                cnt = 0
        if cnt == K:
            result += 1

        cnt = 0

        for y in range(N):
            if arr[y][x] == 1:
                cnt += 1
            if arr[y][x] == 0 and cnt != K:
                cnt = 0
            if arr[y][x] == 0 and cnt == K:
                result += 1
                cnt = 0
        if cnt == K:
            result += 1

    print(f'#{tc+1} {result}')





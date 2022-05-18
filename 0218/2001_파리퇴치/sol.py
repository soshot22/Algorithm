import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_kill = -1
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for l in range(M):
                for m in range(M):
                    kill += arr[i+l][j+m]
            if kill > max_kill:
                max_kill = kill
    print(f'#{tc+1} {max_kill}')
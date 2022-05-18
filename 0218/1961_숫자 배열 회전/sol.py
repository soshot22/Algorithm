import sys
sys.stdin = open('input.txt')
def change(arr, N):
    new_arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-1-j][i]
    return new_arr


for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    fir = change(arr, N)
    sec = change(fir, N)
    thr = change(sec, N)
    print(f'#{tc+1}')
    for i in range(N):
        for j in range(N):
            print(f'{fir[i][j]}', end='')
        print(' ', end = '')
        for j in range(N):
            print(f'{sec[i][j]}', end='')
        print(' ', end='')
        for j in range(N):
            print(f'{thr[i][j]}', end='')
        print()







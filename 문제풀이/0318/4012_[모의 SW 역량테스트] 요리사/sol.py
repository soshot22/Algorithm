import sys
sys.stdin = open('input.txt')

def f(i):
    global selet_a
    global selet_b
    if i == N:
        sel_a = []
        sel_b = []
        if sum(b) == N//2:
            for j in range(N):
                if b[j]:
                    sel_a += [a[j]]
                else:
                    sel_b += [a[j]]
            selet_a += [sel_a]
            selet_b += [sel_b]
            return
        else:
            return

    else:
        b[i] = 1
        f(i+1)
        b[i] = 0
        f(i+1)
    return

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a = [_ for _ in range(N)]
    b = [0] * N
    c = [True, False]
    selet_a = []
    selet_b = []
    f(0)
    result = 10000
    for i in range(len(selet_a)):
        total_a = 0
        total_b = 0
        for j in range(N//2):
            for k in range(j+1, N//2):
                total_a += arr[selet_a[i][j]][selet_a[i][k]]
                total_a += arr[selet_a[i][k]][selet_a[i][j]]
                total_b += arr[selet_b[i][j]][selet_b[i][k]]
                total_b += arr[selet_b[i][k]][selet_b[i][j]]
        content = abs(total_a - total_b)
        if content < result:
            result = content
    print(f'#{tc} {result}')
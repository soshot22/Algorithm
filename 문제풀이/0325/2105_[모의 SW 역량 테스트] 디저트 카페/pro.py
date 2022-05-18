import sys
sys.stdin = open('input.txt')

def DFS(n, ci, cj, v, cnt):
    global si, sj, ans
    if n > 3: # 방향이 0(좌하) 1(우하)2(우상)3(좌상) 4방향
        return
    if n == 3 and ci == si and cj == sj and ans < cnt:
        ans = cnt
        return
    # 현재 방향과 다음 방향
    for k in range(n, n+2):
        ni, nj = ci + di[k], cj + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            DFS(k, ni, nj, v + [arr[ni][nj]], cnt + 1)
        
# 좌하 우하 우상 좌상 , 마지막은 인덱스를 위해 넣음
di, dj = (1, 1, -1, -1, 1),(-1, 1, 1, -1, -1)
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for si in range(N):
        for sj in range(N):

            # 방향, 행, 렬, 방문, 먹은 디저트
            DFS(0, si, sj, [], 0)

    print(f'#{tc} {ans}')
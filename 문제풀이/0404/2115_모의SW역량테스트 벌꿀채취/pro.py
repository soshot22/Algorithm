import sys
sys.stdin = open('input.txt')
'''1. 2명의 일꾼, 겹치지x, M개 연속
2. 선택된 꿀들 최대수익이 되도록 max
3. 가능한 모든 경우 실행
4. 부분집합의 합
'''

def DFS(n, cnt , ssum, lst):
    global sol
    if cnt > C:
        return

    if n == N:
        if sol < ssum:
            sol = ssum
        return
    # 포함 시키지 않는 경우
    DFS(n+1, cnt, ssum, lst)
    # 포함 시키는 경우
    DFS(n+1, cnt+lst[n], ssum+lst[n]**2, lst)

for tc in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 메모이 제이셔 사용법
    mem = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            sol = 0
            DFS(0, 0, 0, arr[i][j:j+M])
            mem[i][j] = sol
    for i1 in range(N):                 # 행
        for j1 in range(N-M+1):         # 열(M개 뽑아야하니)
            for i2 in range(i1, N):
                sj = 0
                if i1 == i2:            # i1과 같은 열이면 그 뒤부터
                    sj = j1+M
                for j2 in range(sj, N-M+1):
                    result = max(result, mem[i1][j1] + mem[i2][j2])  # 최댓값 갱신
    
    # 완전검색 유형
    for i1 in range(N):                 # 행
        for j1 in range(N-M+1):         # 열(M개 뽑아야하니)
            sol = 0                     # i1, j2의 최댓값 뽑기
            DFS(0, 0, 0, arr[i1][j1:j1+M])
            t1 = sol
            for i2 in range(i1, N):
                sj = 0
                if i1 == i2:            # i1과 같은 열이면 그 뒤부터
                    sj = j1+M
                for j2 in range(sj, N-M+1):
                    sol = 0             # i2, l2의 최댓값 뽑기
                    DFS(0, 0, 0, arr[i2][j2:j2+M])
                    result = max(result, t1 + sol)  # 최댓값 갱신
    print(f'#{tc} {result}')
import sys
sys.stdin = open('input.txt')

def DFS(n, ssum):
    global ans
    if n > 12:
        if ssum < ans:
            ans = ssum
        return
    # 일일권
    DFS(n+1, ssum + lst[n]*day)
    # 월간
    DFS(n+1, ssum + mon)
    # 분기
    DFS(n+3, ssum + mon3)
    # 년간
    DFS(n+12, ssum + year)

for tc in range(1, int(input()) + 1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))
    # 임의의 큰수
    ans = 12345678
    # (첫달, 합)
    DFS(1, 0)
    print(f'#{tc} {ans}')
    
    
    # 다른 방식(루프)를 이용한 동적프로그래밍 이용
    D = [0] * 13
    for i in range(1, 13):
        # 일일권
        nmin = D[i-1] + lst[i] * day
        # 월간권 간 일일권을 비교
        nmin = min(nmin, D[i-1] + mon)
        # 석달권 간 비교
        if i >= 3:
            nmin = min(nmin, D[i - 3] + mon3)
        # 연간권 간 비교
        if i >= 12:
            nmin = min(nmin, D[i-12] + year)
        D[i] = nmin
    print(f'#{tc} {nmin}')
            


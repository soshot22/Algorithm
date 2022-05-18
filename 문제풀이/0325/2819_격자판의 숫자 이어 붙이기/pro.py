import sys
sys.stdin = open('input.txt')

def DFS(n, ci, cj, num):
    if n == 7:
        sset.add(num)
        return
    # 상 하  좌 우
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci + di, cj +dj
        # 범위 내라면
        if 0 <= ni < 4 and 0 <= nj < 4:
            # 숫자는 이전 수의 자리 올림(*10) 후 이번 칸 넣기
            DFS(n+1, ni, nj, num*10 + arr[ni][nj])
            # '0010010'의 경우 10010 형태가 됨 어차피 갯수니까 O

for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    # 중복을 확인하기위해 set를 이용
    sset = set()
    for i in range(4):
        for j in range(4):
            DFS(0, i, j, 0)
    print(f'#{tc} {len(sset)}')
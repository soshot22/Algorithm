import sys
sys.stdin = open('input.txt')

# 행, 열, 횟수, 문자열
def bfs(i, j, n, char):
    # 7번 이미 뽑았다면
    if n == 7:
        global result
        # 기존 결과에 없으면 추가
        if char not in result:
            result.append(char)
        return
    # 4방향 반복
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        # 범위 내라면
        if 0 <= ni <= 3 and 0 <= nj <= 3:
            # 해당 문자를 더함
            char += arr[ni][nj]
            bfs(ni, nj, n+1, char)
            # 같은 단계 다른 방향을 위해 다시 지워줘야함
            char = char[:-1]

for tc in range(1, int(input()) + 1):
    # 행렬 4x4 받기
    arr = [list(input().split()) for _ in range(4)]
    # 방향 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    result = []
    # 각각 bfs
    for i in range(4):
        for j in range(4):
            bfs(i, j, 0, '')
    print(f'#{tc} {len(result)}')

import sys
sys.stdin = open('input.txt')

# 상하좌우
di = [[-1, 0],[1, 0], [0, -1], [0, 1]]

def BFS():
    si, sj = 0, 0
    time = [[10*N*N] * N for _ in range(N)]  # 시간을 기록할 2차원 배열
    stack = []                  # 스택 생성
    stack.append([si, sj])      # 시작지점 넣기
    time[si][sj] = 0            # 시작값 최소화
    while stack:                # 스택이 있는 동안 반복
        si, sj = stack.pop(0)   # 시작지점은 가장 왼쪽지점
        for i in range(4):      # 4방향
            ni, nj = si + di[i][0], sj + di[i][1]
            # 지도 범위 내
            if 0 <= ni <= N-1 and 0 <= nj <= N-1:
                # 해당 최소거리가 갱신 가능하다면 스택에 더하고 갱신
                if time[ni][nj] > time[si][sj] + arr[ni][nj]:
                    time[ni][nj] = time[si][sj] + arr[ni][nj]
                    stack.append([ni, nj])
    return time[N-1][N-1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = BFS()
    print(f'#{tc} {result}')
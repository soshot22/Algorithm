import sys
sys.stdin = open('input.txt')
''' 시간이 길게나오긴 함, 가지치기 더 필요할듯?
우선 사각형 모양이 나오기 위해선 새방향이 현 진행 방향 전 방향들 불가
'''


# 방향 좌하 우하 우상 좌상
dir = [[1, -1], [1, 1], [-1, 1], [-1, -1]]

# 행, 렬, 디저트 리스트, 방향 리스트
def BFS(i, j, ls, dir_ls):
    # 4방향을 모두 했고 시작지점이랑 같은 경우
    if len(dir_ls) == 4 and i == start_i and j == start_j:
        # 디저트 수가 더 크면 바꿈
        global result
        if len(ls) > result:
            result = len(ls)
        return
    # 4방향
    for k in range(4):
        # 방향이 아직 없거나 바로 직전 방향인 경우
        if k not in dir_ls or k == dir_ls[-1]:
            ni = i + dir[k][0]
            nj = j + dir[k][1]
            # 행렬 안이고 디저트가 없는 경우
            if 0 <= ni <= N-1 and 0 <= nj <= N-1 and arr[ni][nj] not in ls:
                # 방향이 없는 경우 추가
                if k not in dir_ls:
                    BFS(ni, nj, ls + [arr[ni][nj]], dir_ls + [k])
                else:
                    BFS(ni, nj, ls + [arr[ni][nj]], dir_ls)
    return

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    # 모든 행렬지점 검사
    for i in range(N):
        for j in range(N):
            start_i = i
            start_j = j
            ans = BFS(start_i, start_j, [], [])
    print(f'#{tc} {result}')
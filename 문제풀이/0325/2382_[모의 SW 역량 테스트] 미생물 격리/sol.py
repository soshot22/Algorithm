import sys
sys.stdin = open('input.txt')

def findset(x):
    if rep[x] == x:
        return x
    else:
        return findset(rep[x])
def union(x, y):
    rep[findset(y)] = x

# 방향(상하좌우) 반대방향(하상우좌로 전환을 위한 번호)
di = [[],[-1,0],[1,0],[0,-1],[0,1]]
rev = [[], 2, 1, 4, 3]

for tc in range(1, int(input())+1):
    # 셀의 수 N, 격리 시간 M, 군집 수 K
    N, M, K = map(int, input().split())
    # K개의 군집 세로위치, 가로 위치, 미생물 수 , 이동방향 순
    arr = [list(map(int, input().split())) for _ in range(K)]
    # 시간만큼 반복
    for _ in range(M):
        # 군집만큼 반복
        for i in range(K):
            # 새로운 위치로 이동
            arr[i][0] += di[arr[i][3]][0]
            arr[i][1] += di[arr[i][3]][1]
            # 벽에 부딪힌다면 2배로 줄임, 방향 전환, 깡통으로 다녀도 의미없음
            if arr[i][0] == 0 or arr[i][0] == N-1 or arr[i][1] == 0 or arr[i][1] == N-1:
                arr[i][2] //= 2
                arr[i][3] = rev[arr[i][3]]
        # 중복검사 리스트
        rep = [[l] for l in range(K)]
        for i in range(K):
            for j in range(i+1, K):
                # 좌표가 같은 경우 대표인자 선택
                if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1] and arr[i][2] != 0:
                    rep[i] += [j]
        # 군집만큼 반복
        for i in range(K):
            # 자기자신을 제외하고 중복이 있다면
            if len(rep[i]) > 1:
                # 기본 군집 인덱스
                max_idx = i
                # 중복으로 생긴 것들 제거
                for j in rep[i]:
                    # 본인이 아니라면
                    if i != j:
                        # 해당 중복 비우기
                        rep[j] = []
                    # 중복의 군집이 기존 군집보다 크다면
                    if arr[j][2] > arr[max_idx][2]:
                        # 인덱스 번호 교체
                        max_idx = j
                # 값 교체
                for j in rep[i]:
                    # 최고값 외에는 다 더하고 값을 0으로
                    if max_idx != j:
                        # 최고값 외에는 더하고 0
                        arr[max_idx][2] += arr[j][2]
                        arr[j][2] = 0
    result = 0
    for i in range(K):
        result += arr[i][2]
    print(f'#{tc} {result}')
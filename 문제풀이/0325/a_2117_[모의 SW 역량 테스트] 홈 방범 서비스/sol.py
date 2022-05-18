import sys
sys.stdin = open('input.txt')
# 상하좌우
di = [[-1, 0],[1, 0],[0, -1],[0, 1]]

# 좌표값과 방범 크기 k값
def find(i, j, K):
    if K > k:                           # 최대횟수를 넘은 경우 종료
        return
    visited = [[0]* N for _ in range(N)] # 방문표시
    house = 0                           # 방범 지역 내 집의 수 계산
    visited[i][j] = 1                   # 초기값 방문 표시
    house += arr[i][j]                  # 시작 위치 집의 수 계산
    queue = []                          # 큐 생성
    queue.append([i, j])                # 시작 위치 추가
    flag = 0                            # 탐색 종료 변수
    while queue:
        if flag:                        # 탐색 종료
            break
        i, j = queue.pop(0)             # 가장 오래된 값 출력
        for l in range(4):              # 4방향
            ni, nj = i + di[l][0], j + di[l][1]
                                        # 범위 내이고 미 방문 시 기존 방문값 +1
            if 0 <= ni <= N-1 and 0 <= nj <= N-1 and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                if visited[ni][nj] > K: # 방범범위 밖의 값들 탐색 시 종료
                    flag = 1
                    break
                house += arr[ni][nj]    # 해당 지역에 집이 있으면 +1
                queue.append([ni, nj])  # 큐에 해당 좌표 추가
    money = house * M                   # 현재 방범 범위 내 지불 용의
    cost = K*K + (K-1)*(K-1)             # 현재 방범 비용
    # 방범비용이 지불 가능하며 해당 집의 수가 기존 최댓값보다 클 때
    if money >= cost:
        global result
        if house > result:
            result = house
    find(i, j, K+1)                      # 해당 위치에 방범 범위 1 증가로 확인

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())            # 지도 크기 N, 비용 M
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_money = 0                               # 지불 최댓값
    for i in range(N):                          # 지도의 집 수 계산
        max_money += sum(arr[i])
    max_money *= M                              # 최대 지불값은 지도의 집 수 * 비용
    k = 1                                       # k는 1부터 시작(최소 1집이니)
    while k*k + (k-1)*(k-1) <= max_money:
        k += 1
    k -= 1                                      # 초과할 때까지라 -1
    result = 0                                  # 최종 값
    for i in range(N):                          # 모든 지점을 순회
        for j in range(N):
            find(i, j, 1)
    print(f'#{tc} {result}')
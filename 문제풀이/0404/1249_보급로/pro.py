import sys
sys.stdin = open('input.txt')
'''BFS(먼저 도착하는 것을 찾아야 할 때)
가중치가 있으니(어떤 지점을 가는 것도 중요함), 중복 방문BFS
가중치의 합을 기록할 새로운 v 생성
조건 : 이전 결과보다 더 나은 경과라면 중복 가능(갱신)
v[ni][nj] > v[ci][ci] + arr[ni][nj] 인 경우 경신
초기값을 굉장히 큰 값으로 생성
'''
def BFS(si,sj,ei,ej):
    q = []              # 큐, 방문 배열 생성
    visited = [[100000] * N for _ in range(N)]
    q.append([si, sj])  # 시작값 삽입
    visited[si][sj] = 0 # 시작값 표시
    while q:            # 큐에 값이 있는 동안 반복
        ci, cj = q.pop(0)
        # 4방향
        for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            ni, nj = ci + di, cj + cj
            # 범위 내이고 새 방문지로 가는 루트가 기존보다 짧을 때
            if 0 <= ni <= N-1 and 0 <= nj <= N-1 and visited[ni][nj] > visited[ci][cj] + arr[ni][nj]:
                q.append([ni, nj])
                visited[ni][nj] = visited[ci][cj] + arr[ni][nj]
    return visited[ei][ej]

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = BFS(0, 0, N-1, N-1)
    print(f'#{tc} {result}')

'''
from collections import deque
    q = deque()
    q.popleft()
'''
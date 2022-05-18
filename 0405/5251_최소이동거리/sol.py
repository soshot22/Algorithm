import sys
sys.stdin = open('input.txt')

def dijkstra():
    visited = [0] * (V + 1)  # 방문 표시 리스트
    di = [(E * 100)] * (V + 1)  # 각 인덱스번호까지 가기 위해 드는 가중치 리스트
    di[0] = 0                   # 시작지점 0부터
    # 정점 수 만큼 반복
    for _ in range(V):
        min_idx = -1            # 초기화
        min_value = E * 100     # 초기화
        for i in range(V + 1):  # 처음 시작하는 최솟값 찾기
            if not visited[i] and min_value > di[i]:    # 방문전이고 가중치가 적은 경우
                min_idx = i                     # 인덱스와 가중치 교체
                min_value = di[i]
        visited[min_idx] = 1                    # 해당 정점 방문 표시
        # 현재 지점에서 갈 수 있는 곳 최소 값 갱신
        for j in range(V + 1):   # 방문 전이고 현재 정점에서 해당 정점으로 이동이 더 작은 경우 갱신
            if not visited[j] and di[j] > di[min_idx] + adj[min_idx][j]:
                di[j] = di[min_idx] + adj[min_idx][j]
    # 모든 정점에 대한 최소 가중치 값을 구한 이후 해당 지점 가중치 반환
    return di[V]

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    adj = [[(E * 100)] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w  # 시작 점, 끝점, 가중치
    print(adj)
    result = dijkstra()
    print(adj)
    print(f'#{tc} {result}')
import sys
sys.stdin = open('input.txt')
# tc입력받기
for tc in range(int(input())):
    # 노드의 수 V, 간선의 수 E
    V, E = map(int, input().split())
    # 간선을 표시할 행렬 0 인덱스 제외를 위해 V+1
    arr = [[0] * (V+1) for _ in range(V+1)]
    # E개의 간선을 행렬에 표시
    for i in range(E):
        # 양방향이므로 행과 열을 바꿔서도 입력
        x, y = map(int, input().split())
        arr[x][y] = 1
        arr[y][x] = 1
    # 출발 노드 S와 도착 노드 G 입력
    S, G = map(int, input().split())
    # 노드 방문 리스트 작성
    visited = [0] * (V+1)
    # 큐 생성
    queue = []
    # 시작 지점 방문 표시
    visited[S] = 1
    # 시작 지점을 큐에 추가
    queue.append(S)
    # 출력할 변순
    result = 0
    # 결과를 못낸 동안 반복
    while not result:
        # 시작 지점의 연결 간선 확인 반복문
        for i in range(1, V+1):
            # 간선이 존재하고 방문하지 않았으며 도착점이 아닌 경우
            if arr[S][i] == 1 and visited[i] == 0 and i != G:
                # 해당 노드를 큐에 추가
                queue.append(i)
                # 해당 지점 방문 표시
                visited[i] += visited[S] + 1
            # 해당 간선이 도착점인 경우
            elif arr[S][i] == 1 and i == G:
                # 출발지점 1인 대신 도착 지점을 더하지 않았으므로 그대로 출력
                result = visited[S]
                break
        # 종료조건: 큐에 남은 인자 여부 확인
        if queue:
            S = queue.pop(0)
        else:
            break
        
    print(f'#{tc+1} {result}')
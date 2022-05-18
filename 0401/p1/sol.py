import sys
sys.stdin = open('input.txt')

def DFS(v):
    stack = []                      # 스택생성
    stack.append(v)                 # 시작값 추가
    visited = [0] * 8               # 방문표시 리스트
    visited[v] = 1                  # 시작 값 방문 표시
    s = v                           # 시작값 입력
    print(s, end='')               # 시작값 출력
    while stack:                    # 스택이 있는 동안 반복
        for i in range(1, 8):        # 7개 정점들 순회로 연결 확인
            if i in arr[s] and visited[i] == 0:     # 연결되어있고 미 방문시
                stack.append(i)     # 스택에 쌓고
                print(f'-{i}', end='')  # 현재값 출력
                s = i               # 새 위치로 변경
                visited[s] = 1      # 방문 표시
                break
        else:                       # 더 이상 경로가 없는 경우
            if stack:               # 아직 스택이 남아있다면 해당값 반환
                s = stack.pop()
    print()

def DFS2(v):
    stack = []                      # 스택생성
    stack.append(v)                 # 시작값 추가
    visited = [0] * 8               # 방문표시 리스트
    visited[v] = 1                  # 시작 값 방문 표시
    s = v
    print(s, end='')                # 시작값 출력
    while stack:
        visited[s] = 1  # 방문 표시
        for i in range(8):
            if visited[i] == 0 and i in arr[s]:
                stack.append(i)             # 스택에 쌓고
        else:
            s = stack.pop()
            if visited[s] == 0:
                print(f'-{s}', end='')  # 시작값 출력
    print()


arr = [[] for _ in range(8)]
links = list(map(int, input().split()))
for i in range(len(links)//2):
    n1, n2 = links[i*2], links[i*2 +1]
    arr[n1] += [n2]
    arr[n2] += [n1]
DFS(1)
DFS2(1)
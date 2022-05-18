from collections import deque
import sys
sys.stdin = open('input.txt')

def BFS(N):
    # 0 ~ 1000000 , 방문표시
    visited = [0] * 1000001
    visited[N] = 1
    cnt = 0
    # 큐 생성 후 
    queue = deque()
    queue.append([N, cnt])
    while queue:
        # 큐의 제일 초기값(제일 초기 방문값)
        n, num = queue.popleft()
        # 목표값에 방문했다면 종료
        if visited[M] == 1:
            break
        # +1, *2 , -1, -10 이 백만이하 자연수이고 방문x라면
        # 디큐에 추가, 방문표시(이전 횟수 +1)
        a = n + 1
        if a <= 1000000 and a <= 2*M and visited[a] == 0:
            queue.append([a, num+1])
            visited[a] = 1
        a = n*2
        if a <= 1000000 and a <= 2*M and visited[a] == 0:
            queue.append([a, num+1])
            visited[a] = 1
        a = n-1
        if a > 0 and visited[a] == 0:
            queue.append([a, num+1])
            visited[a] = 1
        a = n-10
        if a > 0 and visited[a] == 0:
            queue.append([a, num+1])
            visited[a] = 1
    return num

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    result = BFS(N)
    print(f'#{tc} {result}')




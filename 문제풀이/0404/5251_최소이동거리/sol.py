import sys
sys.stdin = open('input.txt')

def findset(x):
    if x == rep[x]:
        return x
    else:
        return findset(rep[x])

def MST():
    c = 0                       # 연결된 정점 수
    result = 0                  # 가중치 합할 값
    i = 0                       # 시작
    while c < N:                # 연결된 간선이 N이 될 때 까지
        p1 = findset(edge[i][1]) # 가장 짧은 간선 시작의 대표값
        p2 = findset(edge[i][2]) # 가장 짧은 간선 끝의 대표값
        if p1 != p2:             # 간선 끝값의 대표가 다른 경우
            result += edge[i][0]
            c += 1      
            rep[p2] = p1         # 두 간선 연결
        i += 1
    return result

for tc in range(1, int(input()) + 1):
    # 연결지점 번호 N, 도로의 개수 E
    N, E = map(int, input().split())
    edge = [[] for _ in range(E)]
    rep = list(range(N+1))
    # 간선 정보 저장
    for i in range(E):
        s, e, w = map(int, input().split())
        # 가중치, 시작, 끝 순으로 저장
        edge[i] = [w, s, e]
    edge.sort()
    result = MST()
    print(f'#{tc} {result}')
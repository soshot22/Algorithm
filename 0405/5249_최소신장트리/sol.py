import sys
sys.stdin = open('input.txt')
''' heap을 통해서도 구현 가능
'''

def findset(x):
    if rep[x] == x:
        return x
    else:
        return findset(rep[x])

def union(x, y):
    rep[findset(y)] = findset(x)

for tc in range(1, int(input()) + 1):
    # 마지막 노드 번호 V, 간선의 수 E
    V, E = map(int, input().split())
    # 대표인자 초기화
    rep = [_ for _ in range(V+1)]
    # 간선 정보 리스트
    edge = []
    # 가중치를 정렬을 위해 첫 인자로 하는 리스트
    for _ in range(E):
        s, e, w = map(int, input().split())
        edge.append([w, s, e])
    # 가중치가 낮은 순으로 연결
    edge.sort()
    # 간선 연결 횟수
    cnt = 0
    # 가중치의 합
    result = 0
    # 간선 정보를 순회
    for w, s, e in edge:
        # 시작값과 끝값의 대표값이 다른 경우
        # 한 번이라도 간선 연결을 한 수는 대표값이
        # 연결된 간선들과 똑같아 지므로
        # 둘 모두 간선이 연결된 적이 없는 경우만
        if findset(s) != findset(e):
            # 간선 연결 수 +1
            cnt += 1
            # 가중치 더하기
            result += w
            # 두 간선의 대표값 연결(맞추기)
            union(s, e)
        # V+1개의 간선 모두 연결하기 위해 V번 연결
        if cnt == V:
            break
    print(f'#{tc} {result}')
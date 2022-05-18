import sys
sys.stdin = open('input.txt')

# findset함수 해당 인자의 대표 인자값 찾기
def findset(x):
    # 자기자신이 대표인자이면 그만 
    if rep[x] == x:
        return x
    # 다른 값이 대표값이면 해당 값의 대표값 찾기
    else:
        return findset(rep[x])

# 뒤의 인자의 대표값을 앞의 인자의 대표값으로
def union(x, y):
    # 뒤의 값의 대표인자를 앞의 값의 대표인자로
    rep[findset(y)] = findset(x)
    # # 랭크를 기준으로하는 union
    # x = findset(x)
    # y = findset(y)
    # if rank[x] >= rank[y]:
    #     rep[y] = x
    # else:
    #     rep[x] = y
    # if rank[x] == rank[y]:
    #     rank[x] += 1

for tc in range(1, int(input()) + 1):
    # 총 인원수 N, 총 희망 팀원 신청서 수 M
    N, M = map(int, input().split())
    # 팀원 신청서 리스트 형식으로 받기
    arr = list(map(int, input().split()))
    # 대표 인자를 설정할 리스트 0~N 까지
    rep = [_ for _ in range(N+1)]
    # 희망 팀원 리스트를 순회하여 대표 인자로 연결
    for i in range(M):
        s, e = arr[i*2], arr[i*2 + 1]
        union(s, e)
    team = []
    # 고유 대표인자 값만 추출
    for i in range(1, N+1):
        if findset(i) not in team:
            team += [findset(i)]
    # 고유 대표인자 값의 수가 조의 종류 수
    result = len(team)
    print(f'#{tc} {result}')
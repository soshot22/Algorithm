import sys
sys.stdin = open('input.txt')

def findset(x):
    if rep[x] == x:
        return x
    else:
        return findset(rep[x])

def union(x,y):
    rep[findset(y)] = findset(x)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    rep = [i for i in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        union(x, y)
    ls = []
    for i in range(1, N+1):
        if findset(i) not in ls:
            ls += [findset(i)]
    print(f'#{tc} {len(ls)}')
import sys
sys.stdin = open('input.txt')
for tc in range(int(input())):
    # 상자수, 시행수
    N, Q = map(int, input().split())
    # L R 집합
    M = [list(map(int, input().split())) for _ in range(Q)]
    # 빈상자
    arr = [0] * N
    for i in range(Q):
        L, R = M[i]
        for j in range(L - 1, R):
            arr[j] = i + 1
    print(f'#{tc + 1}', end = ' ')
    for k in arr:
        print(k, end=' ')
    print()



import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())                    # 공장 수 및 제품 수
    arr = [list(map(float, input().split())) for _ in range(N)]
    P = [[0] * N for _ in range(N)]
    for i in range(N):
        Pi = 0
        for j in range(N):
            P[i][j] += arr[j][i]
        P[i] = Pi
    # 우위를 가지는 값
    Px = [[0, 0] for _ in range(N)]
    # 행 순회
    for i in range(N):
        # 열 순회
        for j in range(N):
            b = max(P[j] / arr[i][j], Px[i][0])
            # 최댓값이 변경된 경우
            if b != Px[i][0]:
                Px[i][1] = j
                Px[i][0] = b
    print(Px)
    result = 0
    for i in range(N):
        result += arr[i][Px[i][1]]
    result = int(result)

    print(f'#{tc} {result}')
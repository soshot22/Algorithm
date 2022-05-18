import sys
sys.stdin = open('input.txt')
# tc 입력받기
for tc in range(int(input())):
    # 구해야할 행의 수 입력
    N = int(input())
    # NxN 행렬을 0으로 채워서 생성
    arr = [([0] * N) for _ in range(N)]
    # 시작 값을 1로 설정
    arr[0][0] = 1
    # 0행 다음인 1행부터 시작
    for i in range(1, N):
        # 1행은 0~1 까지이므로 i-1로 설정
        for j in range(i+1):
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    print(f'#{tc+1}')
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                print(arr[i][j], end = ' ')
        print()


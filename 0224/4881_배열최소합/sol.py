import sys
sys.stdin = open('input.txt')

# 사용 현재 행 인자 x, 사용 표시 행렬 ls, 현재 더한 값 plus
def f(x, ls, plus):
    global min_plus
    # 가지치기 plus가 이미 넘은 경우, 안한 경우 swea에서 fail
    if plus >= min_plus:
        return
    # 행렬의 인덱스는 N-1까지이므로 N이 되면 끝난 상황
    if x == N:
        # 최소값이 합과 비교
        if plus < min_plus:
            min_plus = plus
        return
    # 0~N-1까지 N개의 경우의 수
    for i in range(N):
        # 만약 해당 행을 아직 사용하지 않았을 경우
        if ls[i] == 0:
            # 해당 행을 사용 처리 후
            ls[i] = 1
            # 다시 숫자 +1, 행렬, 해당 배열 값을 더해줌
            f(x+1, ls, plus + arr[x][i])
            # for문을 통해 같은 단계의 반복이니 이번 단계에서 사용한
            # 번호는 원상태로 해서 계속 다른 수 찾기 반복
            ls[i] = 0

for tc in range(int(input())):
    # NxN 행렬의 크기 N
    N = int(input())
    # 숫자 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 사용한 것을 표시할 배열
    ls = [0] * N
    #
    min_plus = 10*N
    f(0, ls, 0)
    print(f'#{tc+1} {min_plus}')

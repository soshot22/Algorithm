import sys
sys.stdin = open('input.txt')

# tc 입력
for tc in range(int(input())):
    N = int(input()) // 10
    memo = [0] * N
    memo[0] = 1
    memo[1] = 3
    for i in range(N):
        if i > 1:
            # 홀수
            if i % 2 == 0:
                memo[i] = memo[i-1] * 2 - 1
            elif i % 2 == 1:
                memo[i] = memo[i-2] * 4 - 1
        # memo[i] = memo[i-1] + (memo[i-2]*2 -1)
    result = memo[N-1]
    print(f'#{tc+1} {result}')
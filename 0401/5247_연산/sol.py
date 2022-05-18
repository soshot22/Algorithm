import sys
sys.stdin = open('input.txt')

# 단순 push 꼬리 +1 값 넣기
def push(item):
    global rear
    rear += 1
    stack[rear] = item

# 단순 pop +1 후 추출
def pop():
    global front
    front += 1
    return stack[front]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    dp = [-1] * 2*M
    stack = [0] * 1000000
    rear = -1
    front = -1
    dp[N] = 0
    # 시작값 추가
    push(N)
    # 목표값에 특정값 입력되면 종료
    while dp[M] < 0:
        # 다음 값은 pop으로 추출
        n = pop()
        # 각 4가지 방향 표시
        # +1인 값 표시하고 범위 내이면 스택에 쌓기
        if n+1 <= 1000000 and dp[n+1] == -1:
            dp[n+1] = dp[n] + 1
            push(n+1)
        # *2인 값 표시하고 범위 내이면 스택에 쌓기
        if n*2 <= 1000000 and dp[n*2] == -1:
            dp[n*2] = dp[n] + 1
            push(n*2)
        # -1인 값 표시하고 범위 내이면 스택에 쌓기
        if 0 <= n-1 and dp[n-1] == -1:
            dp[n-1] = dp[n] + 1
            push(n-1)
        # -10인 값 표시하고 범위 내이면 스택에 쌓기
        if 0 <= n-10 and dp[n-10] == -1:
            dp[n - 10] = dp[n] + 1
            push(n-10)
    print(f'#{tc} {dp[M]}')
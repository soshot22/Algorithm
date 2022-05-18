import sys
sys.stdin = open('input.txt')

# 인자(현재 위치, 연료, 충전 횟수)
def f(n, e, cnt):
    global result
    # 최소 횟수 이상 시
    if cnt >= result:
        return
    # 해당 에너지로 목표 정류장을 갈 수 있는 경우(교체 불필요)
    if n + e >= N:
        if cnt < result:
            result = cnt
        return
    # 현재 에너지까지 갈 수 있는 거리(현위치 + 에너지) 끝값에 +1까지 반복
    for i in range(n+1, n + e+1):
        # 해당 정류장, 교체 에너지, 횟수)
        f(i, arr[i], cnt + 1)

for tc in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    # 제일 첫 입력값이 정류장 수 N
    N = arr[0]
    result = N
    f(1, arr[1], 0)
    print(f'#{tc} {result}')
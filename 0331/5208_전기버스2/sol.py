import sys
sys.stdin = open('input.txt')

# 탐욕 방식 인자(목표 위치, 충전 횟수)
def f(N, cnt):
    # 시작 위치로 왔다면 그 횟수 반환
    if N == 1:
        # 1에서 이전 위치 가는 것도 고려했으므로 -1
        return cnt - 1
    # 현재 위치에서 목표 위치까지 순회
    for i in range(1, N):
        # 만약 정류장 i에서 충전량을 더한 값이 목표 이상인 경우
        if i + arr[i] >= N:
            # 목표에서 가장 먼 정류장인 해당 i를 목표로 반복
            goal = f(i, cnt + 1)
            # 반복한 결과 갈 수 있었다면 반복문 끝
            if goal:
                break
    # 해당 함수에서 최소값을 이미 찾았으면 함수 종료
    if goal:
        return goal

for tc in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    # 제일 첫 입력값이 정류장 수 N
    N = arr[0]
    result = f(N, 0)
    print(f'#{tc} {result}')
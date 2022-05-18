import sys
sys.stdin = open('input.txt')

# 버블소트(정렬, 현재 정렬위치)
def BubbleSort(arr, k):
    N = len(arr)
    # 만약 정렬이 끝났다면
    if k == N-1:
        return
    # N-1 ~ k 까지 1씩 줄여나감
    for i in range(N-1, k, -1):
        # 종료값이 왼쪽의 시작 값보다 더 작다면 교체
        if arr[i][1] < arr[i-1][1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
        # 종료값이 동일하다면 시작값이 더 작은 쪽이 왼쪽으로 이동
        elif arr[i][1] == arr[i-1][1] and arr[i][0] < arr[i-1][0]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
    # 다음 정렬로 이동
    BubbleSort(arr, k+1)

for tc in range(1, int(input()) + 1):
    # 신청수 수 N
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 종료값, 시작값 순 기준으로 오름 차순 정렬
    BubbleSort(arr, 0)
    # 작업횟수 결과값 변수
    result = 1
    # 종료값 순으로 다음 종료값의 시작값이 이전 종료값 보다 낮거나 같으면 추가
    # 최초 종료값 설정
    end = arr[0][1]
    for i in range(1, N):
        # 다음 값의 시작값이  종료 시간 뒤면
        if arr[i][0] >= end:
            # 종료 시간 변경 및 작업량 증가
            end = arr[i][1]
            result += 1
    print(f'#{tc} {result}')

import sys
sys.stdin = open('input.txt')

def binarayserach(arr, L, R, key, cnt):
    global result
    # 조사할 구간이 남았거나 한개라면(L=R)
    if L <= R:
        middle = (L + R) // 2
        # 중앙값이 탐색 키와 같으면 종료
        if arr[middle] == key:
            # 좌좌 or 우우를 제외한 경우
            if cnt > -1:
                result += 1
        # 탐색키가 중앙값 보다 작은 경우(왼쪽)
        elif arr[middle] > key:
            # 탐색한 적 없거나 직전에 우측 탐색을 실행한 경우
            if cnt == 0 or cnt == 2:
                cnt = 1
            # 아닌 경우 완전히 끝내기
            else:
                cnt = -1
            # 우측값을 middle -1 로 변경 후 다시 이진탐색
            binarayserach(arr, L, middle-1, key, cnt)
        # 탐색키가 중앙값 보다 큰 경우(오른쪽)
        else:
            # 탐색한 적 없거나 직전에 좌측 탐색을 실행한 경우
            if cnt == 0 or cnt == 1:
                cnt = 2
            # 아닌 경우 완전히 끝내기
            else:
                cnt = -1
            # 좌측값을 middle +1 로 변경 후 다시 이진탐색
            binarayserach(arr, middle+1, R, key, cnt)

for tc in range(1, int(input()) + 1):
    # A, B의 속하는 정수의 수 N, M
    N, M = map(int, input().split())
    # A, B의 리스트
    arr_A = list(map(int, input().split()))
    arr_B = list(map(int, input().split()))
    arr_A.sort()
    result = 0
    # B의 속한 수가 A에서 좌우로 이동하는 지 확인 arr_B 순회
    for i in arr_B:
        binarayserach(arr_A, 0, N-1, i, 0)
    print(f'#{tc} {result}')
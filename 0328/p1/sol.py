# 셀렉션 소트 함수(정렬한 배열, 현재 시작 위치)
def SelectionSort(A, s):
    # n은 총 배열 길이
    n = len(A)
    # 만약 현재 위치가 총 배열 길이의 끝인 경우(배열이 끝남)
    if s == n-1:
        return
    # 최소값 인덱스는 현재 시작 위치
    min_i = s
    # 현재 시작위치부터 n-1까지 확인
    for i in range(s, n):
        # 순회 중인 i번째 배열 값이 기존 최솟값 배열보다 작으면 교체 
        if A[min_i] > A[i]:
            min_i = i
    # 모두 순회한 후 최솟값 인덱스와 현재 시작 위치 인덱스 값 교체
    A[s], A[min_i] = A[min_i], A[s]
    # 새롭게 시작위치를 한칸 더해서 재귀함수로 입력
    SelectionSort(A, s+1)

A = [2, 4, 6, 1, 9, 8, 7, 0]; SelectionSort(A, 0); print(A)

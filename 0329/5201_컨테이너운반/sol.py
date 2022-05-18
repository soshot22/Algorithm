import sys
sys.stdin = open('input.txt')

# 셀렉션 소트(정렬할 배열, 현재까지 정렬한 수)
def SelectionSort(arr, k):
    # 배열의 길이
    N = len(arr)
    # 정렬을 모두 마친 경우
    if k == N-1:
        return
    # 가장 큰 인덱스
    max_k = k
    # 시작점부터 N-1까지 비교
    for i in range(k, N):
        # 만약 해당 인덱스가 최댓값보다 크다면
        if arr[i] > arr[max_k]:
            max_k = i
    # 해당 번째 인덱스는 현재 가장 큰 값으로 변경
    arr[k], arr[max_k] = arr[max_k], arr[k]
    # 다시 함수에 넣기
    SelectionSort(arr, k+1)

for tc in range(1, int(input()) + 1):
    # 컨테이너 수 N, 트럭 수 M
    N, M = map(int, input().split())
    # 컨테이너 무게 리스트
    arr_N = list(map(int, input().split()))
    # 트럭 적재량 리스트
    arr_M = list(map(int, input().split()))
    # 내림차순 정렬
    SelectionSort(arr_N, 0)
    SelectionSort(arr_M, 0)
    print(arr_M)
    print(arr_N)
    # 컨테이너를 옮기지 못할 경우 0이므로
    result = 0
    # 컨테이너 위치를 이동 시킬 변수
    k = 0
    # 트럭의 적재량을 순회할 i
    for i in range(M):
        # 컨테이너 무게를 순회할 j (k~N-1)
        for j in range(k, N):
            # 만약 트럭의 적재량이 컨테이너의 무게보다 크다면 추가
            if arr_M[i] >= arr_N[j]:
                result += arr_N[j]
                # 컨테이너는 다음 인덱스부터 순회하도록 k 조정
                k = j + 1
                break
    print(f'#{tc} {result}')
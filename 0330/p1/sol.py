import sys
sys.stdin = open('input.txt')

# Hoare(리스트, 왼쪽, 오른쪽)
def HoarePartition(ls, L, r):
    # 시작 피봇값(가장 왼쪽 값)
    p = ls[L]
    i, j = L, r
    # 양쪽에서 확인하는 값이 교차할 때 까지
    while i <= j:
        # 양쪽이 뛰어넘지 않고 좌측 값이 기준값 보다 작은 동안
        while i <= j and ls[i] <= p:
            i += 1
        # 양쪽이 뛰어넘지 않고 우측 값이 기준값 보다 큰 동안
        while i <= j and ls[j] >= p:
            j -= 1
        # 교차 전 두 반복문이 멈춘 경우 두 값을 교체
        if i < j:
            ls[i], ls[j] = ls[j], ls[i]
    # j가 멈춘부분(p보다 작은 마지막 수)
    ls[L], ls[j] = ls[j], ls[L]
    # 기준값이 들어간 인덱스 번호를 반환
    return j

# 로무토(리스트, 왼쪽, 오른쪽)
def LomutoPartition(ls, l, r):
    # 기준은 오른쪽 값
    x = ls[r]
    # 왼쪽 인데스보다 1 적게
    i = l - 1
    # 왼쪽부터 오른쪽 끝까지
    for j in range(l, r):
        # 해당 번째가 기준값보다 작으면
        if ls[j] <= x:
            # i 증가 및 자리 교체
            i += 1
            ls[i], ls[j] = ls[j], ls[i]
    # 마지막으로 작았던 i 오른쪽 인데스로 기준값 이동
    ls[i+1], ls[r] = ls[r], ls[i+1]
    # 기준으로 사용한 인덱스 반환
    return i+1

# 퀵정렬 함수
def quickSort(ls, L, r):
    # 아직 정렬할 부분이 남았다면
    if L < r:
        # 새로운 분기점 작성하는 함수
        #s = HoarePartition(ls, L, r)
        s = LomutoPartition(ls, L, r)
        # 분기점의 왼쪽을 다시 퀵정렬
        quickSort(ls, L, s-1)
        # 분기점의 오른쪽을 다시 퀵정렬
        quickSort(ls, s+1, r)

for tc in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    quickSort(arr, 0, len(arr)-1)
    print(f'#{tc} {arr}')
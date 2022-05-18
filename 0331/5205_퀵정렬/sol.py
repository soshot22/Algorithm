import sys
sys.stdin = open('input.txt')

def lomutopartition(arr, L, R):
    # 기준값으로 사용할 p와 인덱스용 변수 i
    p = arr[R]
    i = L - 1
    # 제일 끝(기준으로 사용할) R을 제외한 모든 수 순회
    for j in range(L, R):
        # 순회하는 j번째 값이 p보다 작다면
        if arr[j] <= p:
            # i +1하고 i번째와 j번째 위치 교환
            i += 1
            '''만약 arr[j] > p 몇번한 후라면 j와 i가 차이가
            있을 것이고 j는 p이하인 위치, i는 p보다 작았던
            마지막 수 위치에서 +1이 되어 p보다 큰 첫 수로 갈 것'''
            arr[i], arr[j] = arr[j], arr[i]
    # i번째는 p이하인  마지막 위치 수이므로 그 한칸 옆에 p값 자리 이동
    arr[i+1], arr[R] = arr[R], arr[i+1]
    # 정렬 기준값 위치 반환
    return i + 1


def quicksort(arr, L, R):
    # 정렬할 수가 남아 있다면
    if L < R:
        # 기준값 찾기
        s = lomutopartition(arr, L, R)
        # 기준값 보다 작은 수들 다시 정렬
        quicksort(arr, L, s-1)
        # 기준값 보다 큰 수들 정렬
        quicksort(arr, s+1, R)
    return arr

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = quicksort(arr, 0, N-1)
    print(f'#{tc} {result[N//2]}')
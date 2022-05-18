import sys
sys.stdin = open('input.txt')

# 리스트 병합 함수
def merge(left, right):
    # 병합 과정에서 제일 우측 값 비교 후 좌측 끝이 크면 +1
    if left[-1] > right[-1]:
        global cnt
        cnt += 1
    # 병합하여 반환할 리스트 생성
    result = []
    # 두 리스트에 값이 있는 동안 반복
    l, r = 0, 0
    while l < len(left) or r < len(right):
        # 둘 모두 값이 있다면
        if l < len(left) and r < len(right):
            # 각각 제일 작은 값 비교 후 더 작은 값 추가
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        # 좌측 리스트만 남은 경우 좌측만 추가
        elif l < len(left):
            result.append(left[l])
            l += 1
        # 우측 리스트만 남은 경우 우측만 추가
        elif r < len(right):
            result.append(right[r])
            r += 1
    # 병합한 리스트 반환
    return result

# 분할및 병합 함수 사용해 병합정렬할 함수
def MergeSort(arr):
    # 더 이상 분할을 할 수 없는 경우 반환
    if len(arr) == 1:
        return arr
    # 양쪽으로 나눌 리스트 생성
    left_ls = []
    right_ls = []
    # 좌우를 나눌 기준값
    middle = len(arr) // 2
    # 0 ~ middle 이전 까지는 좌측 리스트
    for i in range(middle):
        left_ls += [arr[i]]
    # middle부터 끝까지는 우측 리스트
    for i in range(middle, len(arr)):
        right_ls += [arr[i]]
    # 좌우 리스트를 또 분할하기 위해 넣기
    left_ls = MergeSort(left_ls)
    right_ls = MergeSort(right_ls)
    # 분할한 리스트들을 병합해서 반환
    return merge(left_ls, right_ls)

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = MergeSort(arr)
    print(f'#{tc} {arr[N//2]} {cnt}')



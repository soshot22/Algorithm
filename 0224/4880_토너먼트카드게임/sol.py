import sys
sys.stdin = open('input.txt')

# 승리 판별 함수
def win(a, b):
    # 인덱스 번호 a < b이므로
    # a가 가위 일때 b가 바위가 아니면 a 반환
    if arr[a] == '1':
        if arr[b] == '2':
            return b
        else:
            return a
    # a가 바위 일때 b가 보가 아니면 a 반환
    elif arr[a] == '2':
        if arr[b] == '3':
            return b
        else:
            return a
    # a가 보 일때 b가 가위가 아니면 a 반환
    else:
        if arr[b] == '1':
            return b
        else:
            return a

# 재귀로 나누기 함수(후위 순회 형식으로 재귀)
def divid(i, j):
    # 중간값 구하기
    middle = (i + j) // 2
    # 시작 값이 중간 값보다 작다면 다시 나누기
    if i < middle:
        left = divid(i, middle)
    # 중간값과 시작 값이 같다면(더 나누기 불가)
    elif middle == i:
        left = i
    # 중간 값 + 1 보다 끝값이 크가면 다시 나누기
    if middle + 1 < j:
        right = divid(middle + 1, j)
    # 중간 값 +1과 끝값이 같다면(더 나누기 불가)
    elif j == middle + 1:
        right = j
    # 더 나누어 지지 않는 값들을 각각 인자로 판별
    result = win(left, right)
    return result

for tc in range(int(input())):
    N = int(input())
    arr = [_ for _ in input().split()]
    start = 0
    end = len(arr) - 1
    print(f'#{tc+1} {divid(start, end) + 1}')
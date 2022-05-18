import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    min_result = sum(arr)
    for i in range(1 << N):
        result = 0
        for j in range(N):
            if i & 1 << j:
                result += arr[j]
        if result >= B and result < min_result:
            min_result = result
    print(f'#{tc} {min_result - B}')
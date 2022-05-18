import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    dis = []
    for i in range(N-1, 0, -1):
        if arr[i] > arr[i-1]:
            dis.append(arr[i] - arr[i-1])
            arr[i], arr[i-1] = arr[i-1], arr[i]
    for i in dis:
        result += i
    print(f'#{tc + 1} {result}')
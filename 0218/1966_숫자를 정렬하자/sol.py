import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j + 1] = arr[j + 1], arr[j]
    print(f'#{tc+1}', end = ' ')
    for z in arr:
        print(z, end=' ')
    print()



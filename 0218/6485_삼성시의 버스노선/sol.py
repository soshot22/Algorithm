import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    # 버스 노선수
    arr = [0] * 5000
    result = []
    N = int(input())
    arr_N = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    arr_P = [int(input()) for _ in range(P)]
    for i in range(N):
        L, R = arr_N[i]
        for j in range(L-1, R):
            arr[j] += 1
    for i in arr_P:
        result.append(arr[i-1])

    print(f'#{tc + 1}', end=' ')
    for k in result:
        print(k, end=' ')
    print()





    


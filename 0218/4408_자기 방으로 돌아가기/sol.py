import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)
    for i in range(N):
        for j in range(2):
            if arr[i][0] < arr[j][0] <









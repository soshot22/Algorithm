import sys
sys.stdin = open('input.txt')

def f(arr, l, r):
    p = [arr[-1]]
    left = []
    right = []
    for i in arr:
        if i > p[0]:
            right.append(i)
        elif i < p[0]:
            left.append(i)
        else:
            p += [p]
        left = f(left, l, p[0])
        right = f(right, p[0] + 1, )
    return left + p + right

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = f(arr)
    print(f'#{tc} {arr[N//2]} {cnt}')
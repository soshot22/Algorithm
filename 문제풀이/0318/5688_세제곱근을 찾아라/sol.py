import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    x = 1
    result = 0
    while x:
        if N % x == 0 and N == x ** 3:
            result = x
            x = 0
            break
        elif N < x**3:
            result = -1
            break
        else:
            x += 1
    print(f'#{tc} {result}')
import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    arr = input()
    for i in range(0, len(arr), 7):
        result = 0
        for j in range(7):
            if arr[i + j] == '1':
                result += 2**(6-j)
        print(result, end=' ')
    print()

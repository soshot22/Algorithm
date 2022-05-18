import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    arr = list(p for p in input())
    cnt = 0
    result = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            cnt += 1
        else:
            if arr[i-1] == '(':
                cnt -= 1
                result += cnt
            else:
                cnt -= 1
                result += 1
    result = result
    print(f'#{tc+1} {result}')






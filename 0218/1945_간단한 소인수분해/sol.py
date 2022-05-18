'''
[입력] T(테스트 케이스 개수) / 숫자 N
2 <= N <= 10000000
1. 반복문형으로 나누기 문제
'''
import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수 변수
T = int(input())
for tc in range(T):
    N = int(input())
    numbers = [2, 3, 5, 7, 11]
    result = []
    for num in numbers:
        k = 0
        while N % num ** k == 0:
            k += 1
        result.append(k - 1)

    print(f'#{tc+1}', end=' ')
    for i in result:
        print(i, end=' ')
    print()





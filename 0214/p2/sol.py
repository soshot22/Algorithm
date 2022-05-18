'''
[입력] 케이스 수 / 10개의 정수
[출력] # {tc} {결과}
[조건] 부분합 집합이 0이 되는 것을 찾는 함수
'''
# input.txt 불러오기
import sys
sys.stdin = open('input.txt')
for tc in range(int(input())):
    arr = list(map(int, input().split()))
    n = 10
    # 모든 경우의 수 중, 공집합 제외
    for i in range(1, 1<<n):
        result = 0
        for j in range(n):
            if i & (1<<j):
                result += arr[j]
        if result == 0:
            print(f'#{tc+1} {1}')
            break
    else:
        print(f'#{tc+1} {0}')
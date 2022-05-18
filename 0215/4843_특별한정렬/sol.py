'''[입력] 총 tc 수 / 정수의 개수 N / 각 정수값 N개
[출력] #{tc} {정렬된 정수}
[조건] 1. 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은수 .....
2. 10개 까지만 출력
'''
# input 불러오기
import sys
sys.stdin = open('input.txt')
# 총 반복할 tc 입력
for tc in range(int(input())):
    # 정수 총 개수 N
    N = int(input())
    # 입력받은 정수를 리스트로 변환
    arr = list(map(int, input().split()))
    # 기본 정렬
    for i in range(N-1):
        # 짝수번째 수(0포함)는 큰수
        if i % 2 == 0:
            # 최우측부터 값 검사
            for j in range(N-1, i, -1):
                if arr[j] > arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
        # 홀수 번째 수는 작은수
        else:
            for j in range(N - 1, i, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
    # 정렬된 값 중 10개만 추출하므로 프린트 형식 맞춰서 출력
    print(f'#{tc+1}', end=' ')
    for n in range(10):
        print(arr[n], end=' ')
    print()



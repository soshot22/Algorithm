'''[입력] TC 수/ 찾을 원소의 수 / 찾을 부분집합의 합
[출력] #{tc} {부분집합의 갯수}
[조건] 1. 1~12까지의 숫자를 원소로 가진 집합A
2. A의 부분집합 중 원소는 N개, 원소의 합이 K인 부분집합 수 출력
3. 해당하는 부분집합이 없는 경우 0 출력
'''
# input 불러오기
import sys
sys.stdin = open('input.txt')
# 총 TC 입력
for tc in range(int(input())):
    # 출력에 사용할 배열 만들기(1~12)
    arr = [0] * 12
    for i in range(12):
        arr[i] = i + 1
    # 목표 원소의 수 N, 목표 부분집합의 합 K입력
    N, K = map(int, input().split())
    # 최종 반환할 부분집합 수 변수
    result = 0
    # 12개의 원소를 가졌으니 2의 12제곱 만큼 부분집합 수
    for i in range(1 << 12):
        # 각 부분집합의 합과 원소를 계산할 변수
        plus = num = 0
        # 12자리와 같은 역할
        for j in range(12):
            # i의 j번째 값이 1이라면 부분집합의 합과 원소수 계산
            if i & (1 << j):
                plus += arr[j]
                num += 1
        # 계산한 부분집합의 원소의 수와 합이 조건 충족여부
        if num == N and plus == K:
            result += 1
    print(f'#{tc+1} {result}')



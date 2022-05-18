'''
[조건] 1. N 개 정수 배열에서 인접한 M개의 합을 계산 
2. M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력
[입력] 테스트 케이스 개수 / N M / N개의 정수
[출력] #{테스트케이스 번호} {M개의 합 최대차이}
[풀이] 1. 입력받은 정수를 오름차순으로 정렬한다.
2. 정렬한 값의 왼쪽에서 M개 합을 오른쪽에서 M개 합에 뺸다.
'''
# input.txt 불러오기
import sys
sys.stdin = open('input.txt')
# 테스트 케이스 횟수 입력
T = int(input())
# 테스트 케이스 수 만큼 반복
for tc in range(T):
    # 각각의 입력 받은 변수들 정리 정수의 수 N, 합을 구할 수 M
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1]
    # 정수들을 리스트 형태로 입력
    numbers = list(map(int, input().split()))
    # 최댓값과 최솟값(N의 최대 100 정수의 최댓값 10000 의 곱 + 1)설정
    m_max = 0
    m_min = 1000001
    # 인접 배열이기에 n개중 오른쪽의 수가 m개 있어야하니 n - m + 1 까지
    for num in range(N - M + 1):
        # 인접 합을 저장할 변수
        plus_num = 0
        # 인접할 수를 정할 반복
        for m in range(M):
            plus_num += numbers[num + m]
        # 인접수가 최댓값보다 크면
        if plus_num > m_max:
            m_max = plus_num
        # 인접수가 최솟값보다 작으면
        if plus_num < m_min:
            m_min = plus_num
    print(f'#{tc + 1} {m_max - m_min}')






    


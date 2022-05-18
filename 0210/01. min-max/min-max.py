'''
[입력] 테스트 케이스 T/ 양수의 수 N/ N개의 양수
[출력] #T 최댓값 - 최솟값
'''
# input.txt를 불러오기
import sys
sys.stdin = open('input.txt')
# 총 반복을 시행할 입력값 변수
T = int(input())
# T번 반복하기 위한 반복문(출력 형식으로 1부터 시작)
for i in range(1, T+1):
    # 양수의 수 N, 비교할 N개의 양수, 최댓값, 최솟값 변수
    N = int(input())
    arr = list(map(int, input().split()))
    # 문제에서 최댓값이 주어지므로 기본 최솟값으로 설정
    ls_min = 1000000
    ls_max = 0
    # 양수의 수인 N번 반복문
    for j in range(N):
        # 해당 값이 최댓값 보다 크면 최댓값 변경
        if arr[j] > ls_max:
            ls_max = arr[j]
        # 해당 값이 최솟값 보다 작으면 최솟값 변경
        if arr[j] < ls_min:
            ls_min = arr[j]
    # 새로운 반복문 시행 전 형식에 맞춰 출력
    print(f'#{i} {ls_max - ls_min}')


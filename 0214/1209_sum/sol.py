'''
[입력] 테스트 케이스 번호 / 100x100 행렬 값
[출력] #{테스트 케이스 번호} / {최댓값}
[조건] 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값
'''
# 입력값 불러오기
import sys
sys.stdin = open('input.txt')
# 10번의 테스트 케이스를 돌릴 반복문
# for n in range(10):
#     # 테스트 케이스 변수
#     tc = input()
#     # 입력 받은 정수 케이스로 만들기
#     numbers = [list(map(int, input().split())) for _ in range(100)]
#     max_sum = sum_right_x = sum_left_x = 0
#     for i in range(100):
#         sum_row = sum_column = 0
#         # 행의 합 최댓값 구하기
#         for j in range(100):
#             sum_row += numbers[i][j]
#         if sum_row > max_sum:
#             max_sum = sum_row
#         # 열의 합 최댓값 구하기
#         for j in range(100):
#             sum_column += numbers[j][i]
#         if sum_column > max_sum:
#             max_sum = sum_column
#         # 좌상우하 대각선 합
#         sum_right_x += numbers[i][i]
#         # 우상좌하 대각선 합
#         sum_left_x += numbers[i][99-i]
#     # 좌상우하 합이 최댓값 보다 크면 교체
#     if max_sum < sum_right_x:
#         max_sum = sum_right_x
#     # 우상좌하 합이 최댓값 보다 크면 교체
#     if max_sum < sum_left_x:
#         max_sum = sum_left_x
#     print(f'#{tc} {max_sum}')

#더 줄여보기
# 테스트 케이스 변수
for n in range(10):
    tc = input()
    # 입력 받은 정수 케이스로 만들기
    numbers = [list(map(int, input().split())) for _ in range(100)]
    max_sum = sum_right_x = sum_left_x = 0
    for i in range(100):
        sum_row = sum_column = 0
        # 행 열의 합 최댓값 구하기
        for j in range(100):
            sum_row += numbers[i][j]
            sum_column += numbers[j][i]
        if sum_row > max_sum:
            max_sum = sum_row
        if sum_column > max_sum:
            max_sum = sum_column
        # 좌상우하 대각선 합
        sum_right_x += numbers[i][i]
        # 우상좌하 대각선 합
        sum_left_x += numbers[i][99-i]
    # 좌상우하 합이 최댓값 보다 크면 교체
    if max_sum < sum_right_x:
        max_sum = sum_right_x
    # 우상좌하 합이 최댓값 보다 크면 교체
    if max_sum < sum_left_x:
        max_sum = sum_left_x
    print(f'#{tc} {max_sum}')




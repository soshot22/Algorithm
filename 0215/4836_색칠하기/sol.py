'''[입력] 총 tc 수 / 칠할 영역의 개수 N/ 왼쪽 아래 모서리 인덱스(r1,c1) ,
 오른쪽 아래 모서리 인덱스(r2, c2) {색칠할 색깔}/
[출력] #{tc} {겹치는 영역 수}
[조건] 입력된 영역을 따라 10x10 격자를 색칠할 경우 다른 색이 중복
되는 영역을 구하는 문제
'''
# input 불러오기
import sys
sys.stdin = open('input.txt')
# 총 tc 만큼 반복
for tc in range(int(input())):
    # 색칠할 0으로 이루어진 2차원 10x10 행렬
    arr = [[0] * 10 for _ in range(10)]
    # 반환할 결과값
    result = 0
    # 색칠할 횟수 입력
    for n in range(int(input())):
        # 각 좌상 x, y 우하 x, y 색칠할 컬러 입력
        start_x, start_y, end_x, end_y, color = map(int, input().split())
        # 좌상 x 좌표부터 우하 x좌표 까지 반복
        for x in range(start_x, end_x+1):
            # 좌상 y 좌표부터 우하 y좌표 까지 반복
            for y in range(start_y, end_y+1):
                # x좌표는 열값 y좌표는 행 값으로 0이 아니고 해당 색의 값이 아니면 중복 수 증가
                if arr[y][x] != 0 and arr[y][x] != color and arr[y][x] != 3:
                    arr[y][x] += color
                # 해당 좌표가 0이면 해당 색의 값으로 변경
                elif arr[y][x] == 0:
                    arr[y][x] = color
    # 전체 배열을 순회
    for i in range(10):
        for j in range(10):
            # 순회한 각 값이 3(중복합)인 경우 result +1
            if arr[i][j] == 3:
                result += 1

    print(f'#{tc+1} {result}')

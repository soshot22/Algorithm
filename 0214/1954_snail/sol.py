'''
[입력] 테스트 케이스 수 / 달팽이 크기 N
[출력] # {tc} {달팽이 배열}
[조건] 1. 달팽이 숫자는 1부터 시계방향으로 N*N까지 숫자가 배열
1. 0으로 구성된 달팽이 배열 생성
2. 우 > 하 > 좌 > 상의 순서로 바로 다음이 0이 아닐때 까지 지속
'''
import sys
sys.stdin = open('input.txt')
# 총반복 수 입력
for tc in range(int(input())):
    N =int(input())
    # 입력받은 NxN 행렬 원소가 모두 0인 행렬
    arr = [[0]*N for _ in range(N)]
    arr[0][0] = 1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    now_x = now_y = 0
    # 숫자 입력용
    n = 1
    while n < N * N:
            while 0 <= now_x + di[0] <= N - 1 and 0 <= now_y + dj[0] <= N - 1 and arr[now_x + di[0]][now_y + dj[0]] == 0:
                n += 1
                now_x += di[0]
                now_y += dj[0]
                arr[now_x][now_y] = n
            while 0 <= now_x + di[1] <= N - 1 and 0 <= now_y + dj[1] <= N - 1 and arr[now_x + di[1]][now_y + dj[1]] == 0:
                n += 1
                now_x += di[1]
                now_y += dj[1]
                arr[now_x][now_y] = n
            while 0 <= now_x + di[2] <= N - 1 and 0 <= now_y + dj[2] <= N - 1 and arr[now_x + di[2]][now_y + dj[2]] == 0:
                n += 1
                now_x += di[2]
                now_y += dj[2]
                arr[now_x][now_y] = n
            while 0 <= now_x + di[3] <= N - 1 and 0 <= now_y + dj[3] <= N - 1 and arr[now_x + di[3]][now_y + dj[3]] == 0:
                n += 1
                now_x += di[3]
                now_y += dj[3]
                arr[now_x][now_y] = n
    print(f'#{tc+1}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()










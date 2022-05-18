import sys
sys.stdin = open('input.txt')

# 좌상 우상 좌하 우하
di = [[-1,-1],[-1, 1],[1,-1],[1,1]]

def NQueen(arr1, n):
    if n == N:
        global result
        result += 1
        return
    for i in range(N):
        # 해당 지점이 놓을 수 있다면
        if arr1[n][i] == 0:
            # 해당 지점에 놓기
            arr[n][i] += 1
            # 이제 불가능한 지점들 표시하기 행 n, 열 i
            # 상방향 표시하기
            for k in range(n-1):
                arr[k][i] += 1
            # 하 표시
            for k in range(n+1, N):
                arr[k][i] += 1
            # 좌 표시
            for k in range(i-1):
                arr[n][k] += 1
            # 우 표시
            for k in range(i+1, N):
                arr[n][k] += 1
            # 좌상 표시
            for k in range(1, N):
                ni, nj = n + di[0][0]*k, i + di[0][1]*k
                if ni < 0 or nj < 0:
                    break
                arr[ni][nj] += 1
            # 우상 표시
            for k in range(1, N):
                ni, nj = n +di[1][0]*k, i +di[1][1]*k
                if ni < 0 or nj > N-1:
                    break
                arr[ni][nj] += 1
            # 좌하 표시
            for k in range(1, N):
                ni, nj = n +di[2][0]*k, i +di[2][1]*k
                if ni > N-1 or nj < 0:
                    break
                arr[ni][nj] += 1
            # 우하 표시
            for k in range(1, N):
                ni, nj = n +di[3][0]*k, i +di[3][1]*k
                if ni > N-1 or nj > N-1:
                    break
                arr[ni][nj] += 1
            NQueen(arr, n+1)
            arr[n][i] -= 1
            # 상방향 표시하기
            for k in range(n - 1):
                arr[k][i] -= 1
            # 하 표시
            for k in range(n + 1, N):
                arr[k][i] -= 1
            # 좌 표시
            for k in range(i - 1):
                arr[n][k] -= 1
            # 우 표시
            for k in range(i + 1, N):
                arr[n][k] -= 1
            # 좌상 표시
            for k in range(1, N):
                ni, nj = n + di[0][0] * k, i + di[0][1] * k
                if ni < 0 or nj < 0:
                    break
                arr[ni][nj] -= 1
            # 우상 표시
            for k in range(1, N):
                ni, nj = n + di[1][0] * k, i + di[1][1] * k
                if ni < 0 or nj > N - 1:
                    break
                arr[ni][nj] -= 1
            # 좌하 표시
            for k in range(1, N):
                ni, nj = n + di[2][0] * k, i + di[2][1] * k
                if ni > N - 1 or nj < 0:
                    break
                arr[ni][nj] -= 1
            # 우하 표시
            for k in range(1, N):
                ni, nj = n + di[3][0] * k, i + di[3][1] * k
                if ni > N - 1 or nj > N - 1:
                    break
                arr[ni][nj] -= 1





for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    result = 0
    NQueen(arr, 0)
    print(f'#{tc} {result}')
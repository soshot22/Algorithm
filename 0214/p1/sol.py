'''
[입력] 총 tc횟수 / 행렬의 크기 / 5x5 배열
[출력] #{tc} {주위 절대값의 합의 총합}
[조건] 1. 총 횟수만큼 반복 2. 행렬의 크기 입력 3. 배열 입력
4. 사용할 주위 숫자 배열 만들기 5. 이중 for문으로 각 숫자들 확인
6. 주위값이 없는 조건 입력
'''
# input 불러오기
import sys
sys.stdin = open('input.txt')
# 1. 입력받은 수만큼 반복
for tc in range(int(input())):
    # 행렬의 크기 입력
    n = int(input())
    # 입력받은 배열 입력
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 사용할 주위 숫자 배열
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    # 이중 for 문으로 각 숫자들 확인
    result = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                new_i = i + di[k]
                new_j = j + dj[k]
                # 조건 입력
                if new_i == -1 or new_i == n:
                    continue
                if new_j == -1 or new_j == n:
                    continue
                result += abs(arr[new_i][new_j] - arr[i][j])
    print(f'#{tc +1 } {result}')







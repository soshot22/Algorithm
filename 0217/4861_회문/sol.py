import sys
sys.stdin = open('input.txt')

def func(arr, n, m):
    # 행 고정 값
    for x in range(n):
        # 열 변화값(10 - 10이면 1회이므로 +1)
        for y in range(n-m +1):
            # 시작 열부터 글자수만큼 슬라이싱
            a = arr[x][y:y + m]
            # 중복 횟수
            cnt = 0
            # 회문을 돌리는 횟수 글자 길이의 반
            for k in range(0, m//2):
                # 각 앞뒤의 글자가 같으면 +1
                if a[0 + k] == a[-1 - k]:
                    cnt += 1
            # 동일한 횟수가 글자 길이 반의 몫
            if cnt == m//2:
                # 해당 슬라이싱 결과로
                return a
    # 열값으로 슬라이싱을 하기 위해 행열값 바꾸기
    for i in range(n):
        for j in range(n):
            if i > j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    # 열값으로 구하는 방법 동일
    for x in range(n):
        for y in range(n-m +1):
            a = arr[x][y:y + m]
            cnt = 0
            for k in range(0, m//2):
                if a[0 + k] == a[-1 - k]:
                    cnt += 1
            if cnt == m//2:
                return a

for tc in range(int(input())):
    # 문자열 크기 N, 회문 크기 M
    N, M = map(int, input().split())
    # 회문 행렬 입력
    Arr = [[p for p in input()] for _ in range(N)]
    result = func(Arr, N, M)
    print(f'#{tc + 1}', end = ' ')
    for q in result:
        print(q, end='')
    print()







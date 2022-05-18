'''
1. 판단 가능하게 추출
2. 추출 횟수 100부터 1씩 줄여나가기
3. 회문 판단 및 찾을 경우 종료
'''
import sys
sys.stdin = open('input.txt')
def func(arr):
    # 추출 문자열 크기 k: 100 >= k >= 1
    for k in range(100, 0, -1):
        # 행 고정 값: 0 <= x <= 99
        for x in range(100):
            # 추출 시작점 y: 0 <= y <= 100-k y+1개
            for y in range(101-k):
                # 비교할 리스트 생성
                new_x = arr[x][y:y+k]
                # 회문 비교
                cnt = 0
                # k//2까지 비교
                for i in range(k // 2):
                    if new_x[i] == new_x[-1 - i]:
                        cnt += 1
                    # 회문 실패 시 반복 종료
                    else:
                        break
                # 회문 판단 시 끝
                if cnt == k // 2:
                    return k
def reverse_arr(arr):
    for i in range(100):
        for j in range(100):
            if i > j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    return arr



for num in range(10):
    tc = input()
    Arr = [[n for n in input()] for _ in range(100)]
    a = func(Arr)
    b = reverse_arr(Arr)
    c = func(b)
    if a >= c:
        print(f'#{tc} {a}')
    else:
        print(f'#{tc} {c}')


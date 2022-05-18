# input 불러오기
import sys
sys.stdin = open('input.txt')

def func(str_1, str_2):
    # 각 글자의 길이 N, M / 각 인덱스로 사용할 i, j
    N = len(str_1)
    M = len(str_2)
    i = j = 0
    # 패턴의 길이보다 작거나 텍스트의 길이보다 작거나(인덱스이므로)
    while i < N and j < M:
        # 인덱스가 불일치 할 경우
        if str_1[i] != str_2[j]:
            # 패턴의 첫 글자와 다르면 계속 진행
            if str_1[i] != str_2[0]:
                i = -1
            # 패턴 첫글자와 같으면 패턴 시작부터 비교
            else:
                i = 0
        i += 1
        j += 1
    # 패턴 인덱스가 패턴의 길이와 같다면
    if i == N:
        return 1
    else:
        return 0


for tc in range(int(input())):
    a = input()
    b = input()
    c = func(a, b)
    print(f'#{tc+1} {c}')


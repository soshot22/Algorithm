import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    # NxM 행렬 N,M 입력
    N, M = map(int, input().split())
    # 암호 문자열로 저장(0b붙여도 10진수로 저장됨)
    password = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
                '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
    # 암호 입력
    arr = [list(map(int, input())) for _ in range(N)]
    # 시작 점 변수
    end = []
    # 행 고정 값 i
    for i in range(N):
        br = 0
        # 열 고정 값 j 뒤에서부터 찾음(56자리 이므로 0~55가 최대, 55까지 조사)
        for j in range(M-1, 54, -1):
            if arr[i][j] == 1:
                end = [i, j]
                br = 1
                break
        if br:
            break
    # 행은 end의 0번째, 열은 (end의 1번 값 - 55)부터 (end의 1번 값)까지
    pass_num = arr[end[0]][end[1]-55:end[1]+1]
    # join을 활용해서 하나의 문자열로 변경
    pass_num = ''.join(map(str, pass_num))
    code = ''
    for i in range(0, len(pass_num), 7):
        if pass_num[i:i+7] in password:
            code += str(password[pass_num[i:i+7]])
    odd = int(code[6])
    even = 0
    # 마지막 수는 제외하고 순회
    for i in range(0,6,2):
        odd += int(code[i])
        even += int(code[i+1])
    if (odd*3 + even + int(code[7])) % 10 == 0:
        print(f'#{tc} {odd + even + int(code[7])}')
    else:
        print(f'#{tc} 0')

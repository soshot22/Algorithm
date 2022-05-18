import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, hex_num = input().split()
    N = int(N)
    result = ''
    for i in range(N):
        # 16진수 > 10진수로 변환
        tmp = int(hex_num[i], base=16)
        # 10진수 > 2진수로 변환(앞의 0b제거), 문자형으로 변경
        tmp = str(bin(tmp).replace('0b', ''))
        # 2진수를 4자리수 형태로 만들기 위한 while문
        while len(tmp) < 4:
            tmp = '0' + tmp
        result += tmp
    print(f'#{tc} {result}')
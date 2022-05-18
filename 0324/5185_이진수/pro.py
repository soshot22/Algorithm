import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N, N16 = input().split()
    result = ''
    for i in N16:
        tmp = int(i, 16)  # 16 진수 > 10진수
        tmp = bin(tmp).replace('0b', '')  # 10진수 > 2진수
        while len(tmp) != 4:  # 2진수 4자리로 만들기
            tmp = '0' + tmp
        result += tmp
    print(f'{tc} {result}')

# 16진수에 해당하는 2진수를 딕셔너리 형태로 저장해서 바로 바로 불러 쓰는 방법도 존재
hex_to_bit = {'0': '0000', '1': '0001', ..., 'F': '1111'}
hex_to_bit = { hex(i).replace('0x', '').upper(): f'{i:04b}' for i in range(16)}
for i in range(N):
    result += hex_to_bit[N16[i]]
result = [hex_to_bit[N16[i]] for i in range(int(N))]
print(f'#{tc} {''.join(result)}')
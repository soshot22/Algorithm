import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    char = input()
    binary = ''
    for i in char:
        a = str(bin(int(i, base=16)).replace('0b',''))
        while len(a) < 4:
            a = '0' + a
        binary += a
    for i in range(0, len(binary), 7):
        print(int(binary[i:i+7], base=2), end=' ')
    print()
    #print(f'#{tc} {result}')
import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    arr = input()
    password = {'001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4, '110111': 5, '001011': 6, '111101': 7,
                '011001': 8, '101111': 9}
    dec = ''
    for i in arr:
        a = bin(int(i, base=16)).replace('0b','')
        while len(a) < 4:
            a = '0' + a
        dec += a
    point = 0
    for i in range(len(dec)-1, -1, -1):
        if dec[i] == '1':
            point = i
            break
    result = ''
    while point - 6 > 0:
        if dec[point-5: point+1] in password:
            result = ' ' + str(password[dec[point-5: point+1]]) + result
            point -= 6
        else:
            point -= 1
    print(result.lstrip())
import sys
sys.stdin = open('input.txt')

def baby(char):
    cnt = 0
    for i in range(2):
        # 트리플 확인
        if int(char[0+3*i]) == int(char[1+3*i]) == int(char[2+3*i]):
            cnt += 1
        # run 확인
        elif int(char[0+3*i]) + 2 == int(char[1+3*i]) + 1 == int(char[2+3*i]):
            cnt += 1
    if cnt == 2:
        return True

def perm(k, text, char):
    if k == 6:
        if baby(char):
            global result
            result = True
    for i in range(k, 6):
        text[k], text[i] = text[i], text[k]
        perm(k+1, text, char + str(text[k]))
        text[k], text[i] = text[i], text[k]



for tc in range(1, int(input()) + 1):
    num = list(map(int, input()))
    result = False
    perm(0, num, '')
    print(f'#{tc} {result}')
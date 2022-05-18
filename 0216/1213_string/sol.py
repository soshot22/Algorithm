'''[입력] 테스트 케이스 번호 / 문자열 / 찾을 문자열
[출력] #{테스트케이스} {답}
[조건]
'''
import sys
sys.stdin = open('input.txt', encoding='UTF-8')

def Cal(char, sentence):
    len_sentence = 0
    len_char = 0
    for len_s in sentence:
        len_sentence += 1
    for len_c in char:
        len_char += 1
    count = 0
    i = j = 0
    while i < len_sentence:
        if sentence[i] != char[j] and sentence[i] != char[0]:
            j = -1
        elif sentence[i] != char[j] and sentence[i] == char[0]:
            j = 0
        elif sentence[i] == char[j] and j == len_char -1:
            count += 1
            j = -1
        i += 1
        j += 1
    return count

for n in range(10):
    tc = input()
    a = input()
    b = input()
    c = Cal(a, b)
    print(f'#{tc} {c}')

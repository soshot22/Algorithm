import sys
sys.stdin = open('input.txt')

def itoa(num):
    result = ''
    num_list = []
    if num < 0:
        num *= -1
        while num // 10 != 0:
            num_list = [num % 10] + num_list
            num //= 10
        num_list = [num] + num_list

        for n in num_list:
            result += chr(n + 48)
        result = '-' + result
        return result

    while num // 10 != 0:
        num_list = [num % 10] + num_list
        num //= 10
    num_list = [num] + num_list

    for n in num_list:
        result += chr(n + 48)
    return result

for tc in range(1, 7):
    a = itoa(int(input()))
    print(f'#{tc} {a} {type(a)}')



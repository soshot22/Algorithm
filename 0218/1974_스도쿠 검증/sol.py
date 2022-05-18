import sys
sys.stdin = open('input.txt')
def three(arr):
    for i in range(2, 9, 3):
        for j in range(2, 9, 3):
            number = 0
            for k in range(3):
                for l in range(3):
                  number += arr[i-k][j-l]
        if number != 45:
            return 0
    return 1

def nine(arr):
    for i in range(9):
        number_x = 0
        number_y = 0
        for j in range(9):
            number_x += arr[i][j]
            number_y += arr[j][i]
        if number_x != 45 or number_y != 45:
            return 0
    return 1

for tc in range(int(input())):
    arr_input = [list(map(int, input().split())) for _ in range(9)]
    a = three(arr_input)
    b = nine(arr_input)
    result = a + b
    if result == 2:
        print(f'#{tc+1} {result-1}')
    else:
        print(f'#{tc+1} 0')
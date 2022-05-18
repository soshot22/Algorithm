import sys
sys.stdin = open('input.txt')
for tc in range(int(input())):
    ls = [[p for p in input()] for _ in range(5)]
    print(f'#{tc+1} ', end='')
    ls_len = 0
    for i in range(len(ls)):
        if len(ls[i]) > ls_len:
            ls_len = len(ls[i])

    for i in range(ls_len):
        for j in range(ls_len):
            try:
                print(ls[j][i], end='')
            except IndexError:
                continue
    print()

# print(f'#{tc+1} {max_kill}')
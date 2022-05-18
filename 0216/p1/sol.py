'''
1.역슬래싱 2.
'''
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(T):
    char = input()
    reverse_char = char[::-1]
    print(f'#{tc+1} {reverse_char}')

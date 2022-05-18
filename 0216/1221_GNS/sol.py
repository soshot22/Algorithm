'''
'''
import sys
sys.stdin = open('input.txt', encoding='UTF-8')
def num_list(str_list):
    new_list = []
    number_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in number_list:
        cnt = 0
        for j in ls:
            if i == j:
                cnt += 1
        cnt_list = [i] * cnt
        new_list += cnt_list
    return new_list

for n in range(int(input())):
    tc, N = input().split()
    N = int(N)
    ls = list(input().split())
    a = num_list(ls)
    print(tc)
    for i in a:
        print(i, end=' ')
    print()

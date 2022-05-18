import sys
sys.stdin = open('input.txt')

def f(num, k, m):
    global result
    if m == 0:
        number = 0
        c = 0
        while c <= N-1:
            number = number *10 + int(num[c]) % 10
            c += 1
        if number > result:
            result = number
        return
    # 최고값을 만들고 m이 남으면
    if k >= N-1:
        if num[0] != sort_num:
            return
        # 같은 값이 있으면 서로 교체
        same = 0
        for i in range(N):
            if same:
                break
            for j in range(N):
                if num[i] == num[j]:
                    same += 1
                    break
        if same:
            f(num, k + 1, m - 1)
        # 없는 경우 끝 자리 2개만 교체
        else:
            num[-2], num[-1] = num[-1], num[-2]
            print(num)
            f(num, k+1, m-1)
    # 최고값 만들기
    for i in range(k+1, N):
        num[k], num[i] = num[i], num[k]
        f(num, k+1, m-1)
        num[k], num[i] = num[i], num[k]
        f(num, k+1, m)

for tc in range(1, int(input()) + 1):
    arr, M = input().split()
    arr = list(map(int, arr))
    M = int(M)
    N = len(arr)
    N_max = max(arr)
    print(N_max)
    result = 0
    sort_num = sorted(arr, reverse=True)
    f(arr, 0, M)
    print(f'#{tc} {result}')
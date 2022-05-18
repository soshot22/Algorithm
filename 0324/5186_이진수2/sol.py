import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    # 1보다 작으므로 실수형으로 받음
    N = float(input())
    # 2** -1부터 확인할 것이므로
    k = -1
    # 결과값을 담을 변수
    result = ''
    # 실수형은 딱 맞는 형태가 아니므로 아주 작은 값 1**-10보다 크면 반복
    while N > 1e-10:
        # k가 13번째 자리에 오는 경우 overflow로 반복문 종료
        if k == -13:
            result = 'overflow'
            break
        # print(f'{(2 ** k)}, {2**k:.30f}')
        # 만약 N이 2**k 보다 크거나 둘의 차이가 아주 작은 값보다 작다면
        if N - 2**k > 0 or abs(N - 2**k) <= 1e-10:
            # N을 그 수만큼 빼고 결과에 1을 더함
            N -= 2**k
            result += '1'
        # N이 2**k보다 작고 둘의 차이가 1e-10보다 큰경우 0을 더함
        else:
            result += '0'
        # 다음 자릿수 검사
        k -= 1
    print(f'#{tc} {result}')